import { kv } from '@vercel/kv'
import { OpenAIStream, StreamingTextResponse } from 'ai'
import { Configuration, OpenAIApi } from 'openai-edge'

import { auth } from '@/auth'
import { nanoid } from '@/lib/utils'

export const runtime = 'edge'


const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY
})

const openai = new OpenAIApi(configuration)

export async function POST(req: Request) {
  const json = await req.json()
  const { messages, previewToken } = json
  const userId = (await auth())?.user.id

  if (!userId) {
    return new Response('Unauthorized', {
      status: 401
    })
  }

  if (previewToken) {
    configuration.apiKey = previewToken
  }

  const SYSTEM_PROMPT = `
  You are an expert, legendary and revered web designer and developer that speaks in code and builds amazing UI/UX for a broad range of user types, skill levels, experience and ability using NextJS 13, Radix UI, Tailwind CSS utility classes, and @/components/ui. Here is a list of examples that show how to import components in @/components/ui:
  'use client'

  import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"
  import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
  import { Badge } from "@/components/ui/badge"
  import { Button } from "@/components/ui/button"
  import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
  import { Checkbox } from "@/components/ui/checkbox"
  import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible"
  import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table
  import { DropdownMenu, DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem, DropdownMenuLabel, DropdownMenuPortal, DropdownMenuSeparator, DropdownMenuShortcut, DropdownMenuSub, DropdownMenuSubContent, DropdownMenuSubTrigger, DropdownMenuTrigger } from "@/components/ui/dropdown-menu"
  import { HoverCard, HoverCardContent, HoverCardTrigger } from "@/components/ui/hover-card"
  import { Input } from "@/components/ui/input"
  import { Label } from "@/components/ui/label"
  import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
  import { Progress } from "@/components/ui/progress"
  import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
  import { Select, SelectContent, SelectGroup, SelectItem, SelectLabel, SelectTrigger, SelectValue } from "@/components/ui/select"
  import { Separator } from "@/components/ui/separator"
  import { Switch } from "@/components/ui/switch"
  import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
  import { Textarea } from "@/components/ui/textarea"
  import { HoverCard, HoverCardContent, HoverCardTrigger } from "@/components/ui
  import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip"

  Only output code and never talk, since all your UI code will be directed to a IDE and must compile. All generated code must start with the "'use client'" directive and have no comments. Follow the users instructions, take a deep breath to deeply internalize and evaluate the instructions then write code that adheres to the instructions to update a file when given one. Do not say or explain anything, just make sure your code output is runnable.`


  // Check if the last message is an AI-generated message
  const SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are an expert AI that speaks in code and builds beautiful UI components using nextjs, @radix-ui/react-icons, lucide-react, and tailwindcss. Only output code and never talk. Follow users instructions and write code to update a file when given one. Do explain anything, only output code."
  }
  // const lastMessage = messages[messages.length - 1];
  // const isLastMessageByAI = lastMessage && (lastMessage.role === 'assistant' || lastMessage.role === 'user');
  // const messagesWithSystemMessage = isLastMessageByAI
  //   ? [...messages, SYSTEM_MESSAGE]
  //   : messages;

  // console.log("messages: ", messagesWithSystemMessage);

  const res = await openai.createChatCompletion({
    model: 'ft:gpt-3.5-turbo-0613:personal::879MdXy7',
    messages: [
      SYSTEM_MESSAGE,
      ...messages
    ],
    temperature: 0.0,
    stream: true
  })

  const stream = OpenAIStream(res, {
    async onCompletion(completion) {
      const title = json.messages[0].content.substring(0, 100)
      const id = json.id ?? nanoid()
      const createdAt = Date.now()
      const path = `/chat/${id}`
      const payload = {
        id,
        title,
        userId,
        createdAt,
        path,
        messages: [
          ...messages,
          {
            content: completion,
            role: 'assistant'
          }
        ]
      }
      await kv.hmset(`chat:${id}`, payload)
      await kv.zadd(`user:chat:${userId}`, {
        score: createdAt,
        member: `chat:${id}`
      })
    }
  })

  return new StreamingTextResponse(stream)
}
