//@ts-nocheck
'use client';
import 'regenerator-runtime/runtime'
import { UseChatHelpers } from 'ai/react'
import * as React from 'react'
import Textarea from 'react-textarea-autosize'
import { MicOff, Mic } from 'lucide-react'

import SpeechRecognition, {
    useSpeechRecognition,
} from "react-speech-recognition";


import { Button, buttonVariants } from '@/components/ui/button'
import { IconArrowElbow } from '@/components/ui/icons'
import {
    Tooltip,
    TooltipContent,
    TooltipTrigger
} from '@/components/ui/tooltip'
import { useEnterSubmit } from '@/lib/hooks/use-enter-submit'
import { cn } from '@/lib/utils'
import { useRouter } from 'next/navigation'

export interface PromptProps
    extends Pick<UseChatHelpers, 'input' | 'setInput'> {
    onSubmit: (value: string) => Promise<void>
    isLoading: boolean
}

export function PromptForm({
    onSubmit,
    input,
    setInput,
    isLoading
}: PromptProps) {
    const { formRef, onKeyDown } = useEnterSubmit()
    const inputRef = React.useRef<HTMLTextAreaElement>(null)
    //const router = useRouter()

    const {
        transcript,
        listening,
    } = useSpeechRecognition();

    React.useEffect(() => {
        if (inputRef.current) {
            inputRef.current.focus()
        }
    }, [])

    React.useEffect(() => {
        if (inputRef.current) {
            inputRef.current.focus()
        }
        if (listening) {
            setInput(transcript)
        }
    }, [transcript, listening])


    return (
        <form
            onSubmit={async e => {
                e.preventDefault()
                if (!input?.trim()) {
                    return
                }
                setInput('')
                await onSubmit(input)
            }}
            ref={formRef}
        >
            <div className="relative flex max-h-60 w-full grow flex-col overflow-hidden bg-background px-8 sm:rounded-md sm:border sm:px-12">
                <Tooltip>
                    <TooltipTrigger>
                        <button
                            onClick={e => {
                                e.preventDefault()
                                if (!listening) {
                                    SpeechRecognition.startListening(e)
                                } else {
                                    SpeechRecognition.stopListening(e)
                                }
                            }}
                            className={cn(
                                buttonVariants({ size: 'sm', variant: 'outline' }),
                                'absolute left-0 top-4 h-8 w-8 rounded-full bg-background p-0 sm:left-4'
                            )}
                        >
                            {!listening ? (
                                <>
                                    <Mic className="h-4 w-4" />
                                    <span className="sr-only">Record</span>
                                </>) : (
                                <>
                                    <Mic className="h-4 w-4 animate-pulse" />
                                    <span className="sr-only">Stop</span>
                                </>)}
                        </button>
                    </TooltipTrigger>
                    <TooltipContent>
                        Record request
                    </TooltipContent>
                </Tooltip>

                <Textarea
                    ref={inputRef}
                    tabIndex={0}
                    onKeyDown={onKeyDown}
                    rows={1}
                    value={input}
                    onChange={e => setInput(e.target.value)}
                    placeholder="Send a message."
                    spellCheck={false}
                    readOnly={listening}
                    className="min-h-[60px] w-full resize-none bg-transparent px-4 py-[1.3rem] focus-within:outline-none sm:text-sm"
                />
                <div className="absolute right-0 top-4 sm:right-4">
                    <Tooltip>
                        <TooltipTrigger asChild>
                            <Button
                                type="submit"
                                size="icon"
                                disabled={isLoading || input === ''}
                            >
                                <IconArrowElbow />
                                <span className="sr-only">Send message</span>
                            </Button>
                        </TooltipTrigger>
                        <TooltipContent>Send message</TooltipContent>
                    </Tooltip>
                </div>
            </div>
        </form >
    )
}
