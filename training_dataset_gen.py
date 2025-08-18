"""TODO"""

from __future__ import annotations

import re
import json

def single_line(s: str):
    """TODO"""

    s = s.replace("\r", "").replace("\n", " ")
    s = re.sub(" +", " ", s)
    s = re.sub("\t+", "\t", s)

    return s.strip()


if __name__ == "__main__":
    data = [
        {
            "messages": [
                {"role": "user", "content": " A minimalistic table of recent invoices"},
                {
                    "role": "assistant",
                    "content": r"""
                        "use client";

                        import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

                        const invoices = [
                            {
                                invoice: "INV001",
                                paymentStatus: "Paid",
                                totalAmount: "$250.00",
                                paymentMethod: "Credit Card",
                            },
                            {
                                invoice: "INV002",
                                paymentStatus: "Pending",
                                totalAmount: "$150.00",
                                paymentMethod: "PayPal",
                            },
                            {
                                invoice: "INV003",
                                paymentStatus: "Unpaid",
                                totalAmount: "$350.00",
                                paymentMethod: "Bank Transfer",
                            },
                            {
                                invoice: "INV004",
                                paymentStatus: "Paid",
                                totalAmount: "$450.00",
                                paymentMethod: "Credit Card",
                            },
                            {
                                invoice: "INV005",
                                paymentStatus: "Paid",
                                totalAmount: "$550.00",
                                paymentMethod: "PayPal",
                            },
                            {
                                invoice: "INV006",
                                paymentStatus: "Pending",
                                totalAmount: "$200.00",
                                paymentMethod: "Bank Transfer",
                            },
                            {
                                invoice: "INV007",
                                paymentStatus: "Unpaid",
                                totalAmount: "$300.00",
                                paymentMethod: "Credit Card",
                            },
                        ];

                        export default function Component() {
                            return (
                                <div className="flex items-center justify-center h-screen">
                                    <Table>
                                        <TableCaption>A list of your recent invoices.</TableCaption>
                                        <TableHeader>
                                            <TableRow>
                                            <TableHead className="w-[100px]">Invoice</TableHead>
                                            <TableHead>Status</TableHead>
                                            <TableHead>Method</TableHead>
                                            <TableHead className="text-right">Amount</TableHead>
                                            </TableRow>
                                        </TableHeader>
                                        <TableBody>
                                            {invoices.map((invoice) => (
                                            <TableRow key={invoice.invoice}>
                                                <TableCell className="font-medium">{invoice.invoice}</TableCell>
                                                <TableCell>{invoice.paymentStatus}</TableCell>
                                                <TableCell>{invoice.paymentMethod}</TableCell>
                                                <TableCell className="text-right">{invoice.totalAmount}</TableCell>
                                            </TableRow>
                                            ))}
                                        </TableBody>
                                    </Table>
                                </div>
                            );
                    }
                    """,
                },
            ]
        },
        {
            "messages": [
                {"role": "user", "content": " An alternative tweet UI"},
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import { Card } from '@/components/ui/card';

                            export default function Component() {
                            return (
                                <div className="flex items-center justify-center h-screen">
                                <Card
                                    className="w-[500px] mx-auto bg-white dark:bg-gray-800 rounded-xl shadow-md overflow-hidden md:max-w-3xl m-3"
                                >
                                    <div className="md:flex">
                                    <div className="md:flex-shrink-0">
                                        <span className="object-cover md:w-48 rounded-md bg-muted w-[192px] h-[192px]" />
                                    </div>
                                    <div className="p-8 w-full">
                                        <div className="flex items-center justify-between">
                                        <div className="flex items-center">
                                            <img
                                            alt="Profile picture"
                                            className="rounded-full"
                                            height="40"
                                            src="/placeholder.svg"
                                            style={{
                                                aspectRatio: '40/40',
                                                objectFit: 'cover',
                                            }}
                                            width="40"
                                            />
                                            <div className="ml-4">
                                            <div className="uppercase tracking-wide text-sm text-black dark:text-white font-semibold">
                                                Caesar Augustus
                                            </div>
                                            <div className="text-gray-400 dark:text-gray-300">
                                                @Augustus
                                            </div>
                                            </div>
                                        </div>
                                        <svg
                                            className=" h-6 w-6 text-blue-500 fill-current"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z" />
                                        </svg>
                                        </div>
                                        <p className="mt-4 text-gray-500 dark:text-gray-300">
                                        I’m in the arena trying stuff. Some will work, some won’t. But
                                        always learning. You’re anonymous and afraid of your own shadow.
                                        Enjoy the sidelines.
                                        </p>
                                        <div className="flex mt-6 justify-between items-center">
                                        <div className="flex space-x-4 text-gray-400 dark:text-gray-300">
                                            <div className="flex items-center">
                                            <svg
                                                className=" h-6 w-6 text-red-500"
                                                fill="none"
                                                height="24"
                                                stroke="currentColor"
                                                strokeLinecap="round"
                                                strokeLinejoin="round"
                                                strokeWidth="2"
                                                viewBox="0 0 24 24"
                                                width="24"
                                                xmlns="http://www.w3.org/2000/svg"
                                            >
                                                <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z" />
                                            </svg>
                                            <span className="ml-1 text-red-500">566</span>
                                            </div>
                                            <div className="flex items-center">
                                            <svg
                                                className=" h-6 w-6 text-green-500"
                                                fill="none"
                                                height="24"
                                                stroke="currentColor"
                                                strokeLinecap="round"
                                                strokeLinejoin="round"
                                                strokeWidth="2"
                                                viewBox="0 0 24 24"
                                                width="24"
                                                xmlns="http://www.w3.org/2000/svg"
                                            >
                                                <path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z" />
                                            </svg>
                                            <span className="ml-1 text-green-500">241</span>
                                            </div>
                                            <div className="flex items-center">
                                            <svg
                                                className=" h-6 w-6 text-blue-500"
                                                fill="none"
                                                height="24"
                                                stroke="currentColor"
                                                strokeLinecap="round"
                                                strokeLinejoin="round"
                                                strokeWidth="2"
                                                viewBox="0 0 24 24"
                                                width="24"
                                                xmlns="http://www.w3.org/2000/svg"
                                            >
                                                <path d="m17 2 4 4-4 4" />
                                                <path d="M3 11v-1a4 4 0 0 1 4-4h14" />
                                                <path d="m7 22-4-4 4-4" />
                                                <path d="M21 13v1a4 4 0 0 1-4 4H3" />
                                            </svg>
                                            <span className="ml-1 text-blue-500">487</span>
                                            </div>
                                        </div>
                                        <div className="text-gray-400 dark:text-gray-300">
                                            7:22 AM · Aug 22, 2023
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </Card>
                                </div>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A login screen with email, google and github login",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import { Icons } from '@/components/icons';
                        import { Button } from '@/components/ui/button';
                        import {
                        Card,
                        CardContent,
                        CardDescription,
                        CardFooter,
                        CardHeader,
                        CardTitle,
                        } from '@/components/ui/card';
                        import { Input } from '@/components/ui/input';
                        import { Label } from '@/components/ui/label';

                        export default function Component() {
                        return (
                            <div className="flex items-center justify-center h-screen">
                            <Card>
                                <CardHeader className="space-y-1">
                                <CardTitle className="text-2xl">Create an account</CardTitle>
                                <CardDescription>
                                    Enter your email below to create your account
                                </CardDescription>
                                </CardHeader>
                                <CardContent className="grid gap-4">
                                <div className="grid grid-cols-2 gap-6">
                                    <Button variant="outline">
                                    <Icons.github className="mr-2 h-4 w-4" />
                                    Github
                                    </Button>
                                    <Button variant="outline">
                                    <Icons.google className="mr-2 h-4 w-4" />
                                    Google
                                    </Button>
                                </div>
                                <div className="relative">
                                    <div className="absolute inset-0 flex items-center">
                                    <span className="w-full border-t" />
                                    </div>
                                    <div className="relative flex justify-center text-xs uppercase">
                                    <span className="bg-background px-2 text-muted-foreground">
                                        Or continue with
                                    </span>
                                    </div>
                                </div>
                                <div className="grid gap-2">
                                    <Label htmlFor="email">Email</Label>
                                    <Input id="email" type="email" placeholder="m@example.com" />
                                </div>
                                <div className="grid gap-2">
                                    <Label htmlFor="password">Password</Label>
                                    <Input id="password" type="password" placeholder="****" />
                                </div>
                                </CardContent>
                                <CardFooter>
                                <Button className="w-full">Create account</Button>
                                </CardFooter>
                            </Card>
                            </div>
                        );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
               {
                    "role": "user",
                    "content": "A contact us form",
                },
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import { Label } from '@/components/ui/label';
                            import { Input } from '@/components/ui/input';
                            import {
                            SelectValue,
                            SelectTrigger,
                            SelectLabel,
                            SelectItem,
                            SelectGroup,
                            SelectContent,
                            Select,
                            } from '@/components/ui/select';
                            import { Textarea } from '@/components/ui/textarea';
                            import { Button } from '@/components/ui/button';
                            import {
                            Card,
                            CardContent,
                            CardHeader,
                            CardTitle,
                            CardDescription,
                            } from '@/components/ui/card';

                            export default function Component() {
                            return (
                                <div className="flex items-center justify-center h-screen">
                                <Card>
                                    <CardHeader>
                                    <CardTitle>Contact Us</CardTitle>
                                    <CardDescription>
                                        Fill out the form below and we'll get back to you as soon as
                                        possible.
                                    </CardDescription>
                                    </CardHeader>

                                    <CardContent>
                                    <div className="space-y-8">
                                        <div className="space-y-4">
                                        <div className="grid grid-cols-2 gap-4">
                                            <div className="space-y-2">
                                            <Label htmlFor="first-name">First name</Label>
                                            <Input id="first-name" placeholder="Enter your first name" />
                                            </div>
                                            <div className="space-y-2">
                                            <Label htmlFor="last-name">Last name</Label>
                                            <Input id="last-name" placeholder="Enter your last name" />
                                            </div>
                                        </div>
                                        <div className="space-y-2">
                                            <Label htmlFor="email">Email</Label>
                                            <Input id="email" placeholder="Enter your email" type="email" />
                                        </div>
                                        <div className="space-y-2">
                                            <Label>Pronoun</Label>
                                            <Select>
                                            <SelectTrigger aria-label="Pronoun">
                                                <SelectValue placeholder="Select your pronoun" />
                                            </SelectTrigger>
                                            <SelectContent>
                                                <SelectGroup>
                                                <SelectLabel>Pronouns</SelectLabel>
                                                <SelectItem value="he/him">He/Him</SelectItem>
                                                <SelectItem value="she/her">She/Her</SelectItem>
                                                <SelectItem value="they/them">They/Them</SelectItem>
                                                <SelectItem value="prefer not to say">
                                                    Prefer not to say
                                                </SelectItem>
                                                </SelectGroup>
                                            </SelectContent>
                                            </Select>
                                        </div>
                                        <div className="space-y-2">
                                            <Label htmlFor="message">Message</Label>
                                            <Textarea
                                            className="min-h-[100px]"
                                            id="message"
                                            placeholder="Enter your message"
                                            />
                                        </div>
                                        <Button className="bg-gray-800 text-white" type="submit">
                                            Send message
                                        </Button>
                                        </div>
                                    </div>
                                    </CardContent>
                                </Card>
                                </div>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A FAQ section with an accordion",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        "use client";

                        import { AccordionTrigger, AccordionContent, AccordionItem, Accordion } from "@/components/ui/accordion";
                        import { CardContent, Card } from "@/components/ui/card";

                        export default function Component() {
                            return (
                                <div className="flex justify-center items-center min-h-screen">
                                <Card className="shadow-lg w-[550px]">
                                    <CardContent className="p-6">
                                    <h2 className="text-2xl font-semibold">Frequently Asked Questions</h2>
                                    <Accordion className="w-full mt-4" collapsible="" type="multiple">
                                        <AccordionItem value="item-1">
                                        <AccordionTrigger className="hover:underline-none">
                                            Why does turning my device off and on again solve all issues?
                                        </AccordionTrigger>
                                        <AccordionContent>Because it clears the memory and starts the system from scratch.</AccordionContent>
                                        </AccordionItem>
                                        <AccordionItem value="item-2">
                                        <AccordionTrigger className="hover:underline-none">
                                            Are extra cables in the box bonus decorations?
                                        </AccordionTrigger>
                                        <AccordionContent>
                                            As tempting as it is to weave them into artistic sculptures, those cables are essential for connecting,
                                            charging, and beaming digital magic.
                                        </AccordionContent>
                                        </AccordionItem>
                                        <AccordionItem value="item-3">
                                        <AccordionTrigger className="hover:underline-none">
                                            Can I wear my VR headset to my cousin's wedding?
                                        </AccordionTrigger>
                                        <AccordionContent>
                                            Yes but you might end up inadvertently dodging invisible dance partners or trying to high-five digital
                                            confetti.
                                        </AccordionContent>
                                        </AccordionItem>
                                        <AccordionItem value="item-4">
                                        <AccordionTrigger className="hover:underline-none">
                                            How often should I update my software?
                                        </AccordionTrigger>
                                        <AccordionContent>
                                            It's recommended to keep your software up to date to ensure you have the latest security patches and
                                            features.
                                        </AccordionContent>
                                        </AccordionItem>
                                        <AccordionItem className="border-b-0" value="item-5">
                                        <AccordionTrigger className="hover:underline-none">
                                            Why does my device get hot when I'm using it?
                                        </AccordionTrigger>
                                        <AccordionContent>
                                            Devices can generate heat during operation, especially when running intensive tasks. This is normal, but
                                            if it gets too hot, it may indicate a problem.
                                        </AccordionContent>
                                        </AccordionItem>
                                    </Accordion>
                                    </CardContent>
                                </Card>
                                </div>
                            );
                    }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A payment method screen with card, paypal, and apple method",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import { Icons } from '@/components/icons';
                        import { Button } from '@/components/ui/button';
                        import {
                        Card,
                        CardContent,
                        CardDescription,
                        CardFooter,
                        CardHeader,
                        CardTitle,
                        } from '@/components/ui/card';
                        import { Input } from '@/components/ui/input';
                        import { Label } from '@/components/ui/label';
                        import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';
                        import {
                        Select,
                        SelectContent,
                        SelectItem,
                        SelectTrigger,
                        SelectValue,
                        } from '@/components/ui/select';

                        export default function Component() {
                        return (
                            <div className="flex justify-center items-center min-h-screen">
                            <Card className="w-full max-w-lg">
                                <CardHeader>
                                <CardTitle>Payment Method</CardTitle>
                                <CardDescription>
                                    Add a new payment method to your account.
                                </CardDescription>
                                </CardHeader>
                                <CardContent className="grid gap-6">
                                <RadioGroup defaultValue="card" className="grid grid-cols-3 gap-4">
                                    <div>
                                    <RadioGroupItem value="card" id="card" className="peer sr-only" />
                                    <Label
                                        htmlFor="card"
                                        className="flex flex-col items-center justify-between rounded-md border-2 border-muted bg-popover p-4 hover:bg-accent hover:text-accent-foreground peer-data-[state=checked]:border-primary [&:has([data-state=checked])]:border-primary"
                                    >
                                        <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth="2"
                                        className="mb-3 h-6 w-6"
                                        >
                                        <rect width="20" height="14" x="2" y="5" rx="2" />
                                        <path d="M2 10h20" />
                                        </svg>
                                        Card
                                    </Label>
                                    </div>
                                    <div>
                                    <RadioGroupItem
                                        value="paypal"
                                        id="paypal"
                                        className="peer sr-only"
                                    />
                                    <Label
                                        htmlFor="paypal"
                                        className="flex flex-col items-center justify-between rounded-md border-2 border-muted bg-popover p-4 hover:bg-accent hover:text-accent-foreground peer-data-[state=checked]:border-primary [&:has([data-state=checked])]:border-primary"
                                    >
                                        <Icons.paypal className="mb-3 h-6 w-6" />
                                        Paypal
                                    </Label>
                                    </div>
                                    <div>
                                    <RadioGroupItem
                                        value="apple"
                                        id="apple"
                                        className="peer sr-only"
                                    />
                                    <Label
                                        htmlFor="apple"
                                        className="flex flex-col items-center justify-between rounded-md border-2 border-muted bg-popover p-4 hover:bg-accent hover:text-accent-foreground peer-data-[state=checked]:border-primary [&:has([data-state=checked])]:border-primary"
                                    >
                                        <Icons.apple className="mb-3 h-6 w-6" />
                                        Apple
                                    </Label>
                                    </div>
                                </RadioGroup>
                                <div className="grid gap-2">
                                    <Label htmlFor="name">Name</Label>
                                    <Input id="name" placeholder="First Last" />
                                </div>
                                <div className="grid gap-2">
                                    <Label htmlFor="number">Card number</Label>
                                    <Input id="number" placeholder="123-4567-890" />
                                </div>
                                <div className="grid grid-cols-3 gap-4">
                                    <div className="grid gap-2">
                                    <Label htmlFor="month">Expires</Label>
                                    <Select>
                                        <SelectTrigger id="month">
                                        <SelectValue placeholder="Month" />
                                        </SelectTrigger>
                                        <SelectContent>
                                        <SelectItem value="1">January</SelectItem>
                                        <SelectItem value="2">February</SelectItem>
                                        <SelectItem value="3">March</SelectItem>
                                        <SelectItem value="4">April</SelectItem>
                                        <SelectItem value="5">May</SelectItem>
                                        <SelectItem value="6">June</SelectItem>
                                        <SelectItem value="7">July</SelectItem>
                                        <SelectItem value="8">August</SelectItem>
                                        <SelectItem value="9">September</SelectItem>
                                        <SelectItem value="10">October</SelectItem>
                                        <SelectItem value="11">November</SelectItem>
                                        <SelectItem value="12">December</SelectItem>
                                        </SelectContent>
                                    </Select>
                                    </div>
                                    <div className="grid gap-2">
                                    <Label htmlFor="year">Year</Label>
                                    <Select>
                                        <SelectTrigger id="year">
                                        <SelectValue placeholder="Year" />
                                        </SelectTrigger>
                                        <SelectContent>
                                        {Array.from({ length: 10 }, (_, i) => (
                                            <SelectItem
                                            key={i}
                                            value={`${new Date().getFullYear() + i}`}
                                            >
                                            {new Date().getFullYear() + i}
                                            </SelectItem>
                                        ))}
                                        </SelectContent>
                                    </Select>
                                    </div>
                                    <div className="grid gap-2">
                                    <Label htmlFor="cvc">CVC</Label>
                                    <Input id="cvc" placeholder="CVC" />
                                    </div>
                                </div>
                                </CardContent>
                                <CardFooter>
                                <Button className="w-full">Continue</Button>
                                </CardFooter>
                            </Card>
                            </div>
                        );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "A card form for reporting an issue"},
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import { Button } from '@/components/ui/button';
                            import {
                            Card,
                            CardContent,
                            CardDescription,
                            CardFooter,
                            CardHeader,
                            CardTitle,
                            } from '@/components/ui/card';
                            import { Input } from '@/components/ui/input';
                            import { Label } from '@/components/ui/label';
                            import { Textarea } from '@/components/ui/textarea';

                            export default function Component() {
                            return (
                                <div className="flex justify-center items-center min-h-screen">
                                <Card className="w-full max-w-lg">
                                    <CardHeader>
                                    <CardTitle>Report an issue</CardTitle>
                                    <CardDescription>
                                        What area are you having problems with?
                                    </CardDescription>
                                    </CardHeader>
                                    <CardContent className="grid gap-6">
                                    <div className="grid gap-2">
                                        <Label htmlFor="subject">Subject</Label>
                                        <Input id="subject" placeholder="I need help with..." />
                                    </div>
                                    <div className="grid gap-2">
                                        <Label htmlFor="description">Description</Label>
                                        <Textarea
                                        id="description"
                                        placeholder="Please include all information relevant to your issue."
                                        />
                                    </div>
                                    </CardContent>
                                    <CardFooter className="justify-between space-x-2">
                                    <Button variant="ghost">Cancel</Button>
                                    <Button>Submit</Button>
                                    </CardFooter>
                                </Card>
                                </div>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "A cookie preferences form"},
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import { Button } from '@/components/ui/button';
                        import {
                        Card,
                        CardContent,
                        CardDescription,
                        CardFooter,
                        CardHeader,
                        CardTitle,
                        } from '@/components/ui/card';
                        import { Label } from '@/components/ui/label';
                        import { Switch } from '@/components/ui/switch';

                        export default function Component() {
                        return (
                            <div className="flex justify-center items-center min-h-screen">
                            <Card className="w-full max-w-lg">
                                <CardHeader>
                                <CardTitle>Cookie Settings</CardTitle>
                                <CardDescription>Manage your cookie settings here.</CardDescription>
                                </CardHeader>
                                <CardContent className="grid gap-6">
                                <div className="flex items-center justify-between space-x-2">
                                    <Label htmlFor="necessary" className="flex flex-col space-y-1">
                                    <span>Strictly Necessary</span>
                                    <span className="font-normal leading-snug text-muted-foreground">
                                        These cookies are essential in order to use the website and use
                                        its features.
                                    </span>
                                    </Label>
                                    <Switch id="necessary" defaultChecked />
                                </div>
                                <div className="flex items-center justify-between space-x-2">
                                    <Label htmlFor="functional" className="flex flex-col space-y-1">
                                    <span>Functional Cookies</span>
                                    <span className="font-normal leading-snug text-muted-foreground">
                                        These cookies allow the website to provide personalized
                                        functionality.
                                    </span>
                                    </Label>
                                    <Switch id="functional" />
                                </div>
                                <div className="flex items-center justify-between space-x-2">
                                    <Label htmlFor="performance" className="flex flex-col space-y-1">
                                    <span>Performance Cookies</span>
                                    <span className="font-normal leading-snug text-muted-foreground">
                                        These cookies help to improve the performance of the website.
                                    </span>
                                    </Label>
                                    <Switch id="performance" />
                                </div>
                                </CardContent>
                                <CardFooter>
                                <Button variant="outline" className="w-full">
                                    Save preferences
                                </Button>
                                </CardFooter>
                            </Card>
                            </div>
                        );
                    }
                    """,
                },
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "A statistic card showing total revenues"},
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import {
                        Card,
                        CardContent,
                        CardDescription,
                        CardFooter,
                        CardHeader,
                        CardTitle,
                        } from '@/components/ui/card';

                        export default function Component() {
                        return (
                            <div className="flex justify-center items-center min-h-screen">
                            <Card className="w-full max-w-xs">
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium">Total Revenue</CardTitle>
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 24 24"
                                    fill="none"
                                    stroke="currentColor"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    className="h-4 w-4 text-muted-foreground"
                                >
                                    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                                </svg>
                                </CardHeader>
                                <CardContent>
                                <div className="text-2xl font-bold">$45,231.89</div>
                                <p className="text-xs text-muted-foreground">
                                    +20.1% from last month
                                </p>
                                </CardContent>
                            </Card>
                            </div>
                        );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "A statistic card showing subscriptions"},
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import {
                        Card,
                        CardContent,
                        CardDescription,
                        CardFooter,
                        CardHeader,
                        CardTitle,
                        } from '@/components/ui/card';

                        export default function Component() {
                        return (
                            <div className="flex justify-center items-center min-h-screen">
                            <Card className="w-full max-w-xs">
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium">Subscriptions</CardTitle>
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 24 24"
                                    fill="none"
                                    stroke="currentColor"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    className="h-4 w-4 text-muted-foreground"
                                >
                                    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
                                    <circle cx="9" cy="7" r="4" />
                                    <path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75" />
                                </svg>
                                </CardHeader>
                                <CardContent>
                                <div className="text-2xl font-bold">+2350</div>
                                <p className="text-xs text-muted-foreground">
                                    +180.1% from last month
                                </p>
                                </CardContent>
                            </Card>
                            </div>
                        );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "A statistic card showing sales"},
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import {
                            Card,
                            CardContent,
                            CardDescription,
                            CardFooter,
                            CardHeader,
                            CardTitle,
                            } from '@/components/ui/card';

                            export default function Component() {
                            return (
                                <div className="flex justify-center items-center min-h-screen">
                                <Card className="w-full max-w-xs">
                                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                    <CardTitle className="text-sm font-medium">Sales</CardTitle>
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth="2"
                                        className="h-4 w-4 text-muted-foreground"
                                    >
                                        <rect width="20" height="14" x="2" y="5" rx="2" />
                                        <path d="M2 10h20" />
                                    </svg>
                                    </CardHeader>
                                    <CardContent>
                                    <div className="text-2xl font-bold">+12,234</div>
                                    <p className="text-xs text-muted-foreground">+19% from last month</p>
                                    </CardContent>
                                </Card>
                                </div>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "A statistic card showing active sales"},
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import {
                        Card,
                        CardContent,
                        CardDescription,
                        CardFooter,
                        CardHeader,
                        CardTitle,
                        } from '@/components/ui/card';

                        export default function Component() {
                        return (
                            <div className="flex justify-center items-center min-h-screen">
                            <Card className="w-full max-w-xs">
                                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                                <CardTitle className="text-sm font-medium">Active Now</CardTitle>
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 24 24"
                                    fill="none"
                                    stroke="currentColor"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    className="h-4 w-4 text-muted-foreground"
                                >
                                    <path d="M22 12h-4l-3 9L9 3l-3 9H2" />
                                </svg>
                                </CardHeader>
                                <CardContent>
                                <div className="text-2xl font-bold">+573</div>
                                <p className="text-xs text-muted-foreground">+201 since last hour</p>
                                </CardContent>
                            </Card>
                            </div>
                        );
                    }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A minimalistic list of recent user sales",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';

                        export default function Component() {
                        return (
                            <div className="flex justify-center items-center min-h-screen">
                            <div className="space-y-8 w-full max-w-lg border rounded-md p-8">
                                <div className="flex items-center">
                                <Avatar className="h-9 w-9">
                                    <AvatarImage src="/avatars/01.png" alt="Avatar" />
                                    <AvatarFallback>OM</AvatarFallback>
                                </Avatar>
                                <div className="ml-4 space-y-1">
                                    <p className="text-sm font-medium leading-none">Olivia Martin</p>
                                    <p className="text-sm text-muted-foreground">
                                    olivia.martin@email.com
                                    </p>
                                </div>
                                <div className="ml-auto font-medium">+$1,999.00</div>
                                </div>
                                <div className="flex items-center">
                                <Avatar className="flex h-9 w-9 items-center justify-center space-y-0 border">
                                    <AvatarImage src="/avatars/02.png" alt="Avatar" />
                                    <AvatarFallback>JL</AvatarFallback>
                                </Avatar>
                                <div className="ml-4 space-y-1">
                                    <p className="text-sm font-medium leading-none">Jackson Lee</p>
                                    <p className="text-sm text-muted-foreground">
                                    jackson.lee@email.com
                                    </p>
                                </div>
                                <div className="ml-auto font-medium">+$39.00</div>
                                </div>
                                <div className="flex items-center">
                                <Avatar className="h-9 w-9">
                                    <AvatarImage src="/avatars/03.png" alt="Avatar" />
                                    <AvatarFallback>IN</AvatarFallback>
                                </Avatar>
                                <div className="ml-4 space-y-1">
                                    <p className="text-sm font-medium leading-none">Isabella Nguyen</p>
                                    <p className="text-sm text-muted-foreground">
                                    isabella.nguyen@email.com
                                    </p>
                                </div>
                                <div className="ml-auto font-medium">+$299.00</div>
                                </div>
                                <div className="flex items-center">
                                <Avatar className="h-9 w-9">
                                    <AvatarImage src="/avatars/04.png" alt="Avatar" />
                                    <AvatarFallback>WK</AvatarFallback>
                                </Avatar>
                                <div className="ml-4 space-y-1">
                                    <p className="text-sm font-medium leading-none">William Kim</p>
                                    <p className="text-sm text-muted-foreground">will@email.com</p>
                                </div>
                                <div className="ml-auto font-medium">+$99.00</div>
                                </div>
                                <div className="flex items-center">
                                <Avatar className="h-9 w-9">
                                    <AvatarImage src="/avatars/05.png" alt="Avatar" />
                                    <AvatarFallback>SD</AvatarFallback>
                                </Avatar>
                                <div className="ml-4 space-y-1">
                                    <p className="text-sm font-medium leading-none">Sofia Davis</p>
                                    <p className="text-sm text-muted-foreground">
                                    sofia.davis@email.com
                                    </p>
                                </div>
                                <div className="ml-auto font-medium">+$39.00</div>
                                </div>
                            </div>
                            </div>
                        );
                    }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A notification settings card",
                },
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import { BellIcon, EyeNoneIcon, PersonIcon } from '@radix-ui/react-icons';

                            import {
                            Card,
                            CardContent,
                            CardDescription,
                            CardHeader,
                            CardTitle,
                            } from '@/components/ui/card';

                            export default function Component() {
                            return (
                                <div className="flex justify-center items-center min-h-screen">
                                <Card className="w-full max-w-lg">
                                    <CardHeader className="pb-3">
                                    <CardTitle>Notifications</CardTitle>
                                    <CardDescription>
                                        Choose what you want to be notified about.
                                    </CardDescription>
                                    </CardHeader>
                                    <CardContent className="grid gap-1">
                                    <div className="-mx-2 flex items-start space-x-4 rounded-md p-2 transition-all hover:bg-accent hover:text-accent-foreground">
                                        <BellIcon className="mt-px h-5 w-5" />
                                        <div className="space-y-1">
                                        <p className="text-sm font-medium leading-none">Everything</p>
                                        <p className="text-sm text-muted-foreground">
                                            Email digest, mentions & all activity.
                                        </p>
                                        </div>
                                    </div>
                                    <div className="-mx-2 flex items-start space-x-4 rounded-md bg-accent p-2 text-accent-foreground transition-all">
                                        <PersonIcon className="mt-px h-5 w-5" />
                                        <div className="space-y-1">
                                        <p className="text-sm font-medium leading-none">Available</p>
                                        <p className="text-sm text-muted-foreground">
                                            Only mentions and comments.
                                        </p>
                                        </div>
                                    </div>
                                    <div className="-mx-2 flex items-start space-x-4 rounded-md p-2 transition-all hover:bg-accent hover:text-accent-foreground">
                                        <EyeNoneIcon className="mt-px h-5 w-5" />
                                        <div className="space-y-1">
                                        <p className="text-sm font-medium leading-none">Ignoring</p>
                                        <p className="text-sm text-muted-foreground">
                                            Turn off all notifications.
                                        </p>
                                        </div>
                                    </div>
                                    </CardContent>
                                </Card>
                                </div>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A testinomial card",
                },
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import {
                            CardContent,
                            CardTitle,
                            CardDescription,
                            CardHeader,
                            Card,
                            } from '@/components/ui/card';
                            import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';

                            export default function Component() {
                            return (
                                <div className="flex items-center justify-center min-h-screen">
                                <Card className="p-6  max-w-lg font-poppins">
                                    <CardContent className="text-xl relative mb-2">
                                    <svg
                                        className=" absolute top-0 left-0 text-20xl text-cyan-300"
                                        fill="none"
                                        height="24"
                                        stroke="currentColor"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth="2"
                                        viewBox="0 0 24 24"
                                        width="24"
                                        xmlns="http://www.w3.org/2000/svg"
                                    >
                                        <path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z" />
                                        <path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z" />
                                    </svg>
                                    "Generating a testimonial card component with a prompt-driven
                                    interface is pretty cool... Well done, Augustus!"
                                    </CardContent>
                                    <CardHeader className="pt-0">
                                    <div className="flex items-center">
                                        <Avatar className="h-9 w-9">
                                        <AvatarImage src="/avatars/01.png" alt="Avatar" />
                                        <AvatarFallback>CA</AvatarFallback>
                                        </Avatar>

                                        <div>
                                        <CardTitle className="text-base">Caesar Augustus</CardTitle>
                                        <CardDescription>Prima Porta</CardDescription>
                                        </div>
                                    </div>
                                    </CardHeader>
                                </Card>
                                </div>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A sleek pricing page for a SaaS",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import { Button } from '@/components/ui/button';

                        export default function Component() {
                        return (
                            <section className="min-h-screen w-full py-12 flex items-center justify-center">
                            <div className="container px-4 md:px-6">
                                <div className="grid grid-cols-1 gap-6 mt-8 md:grid-cols-3 md:gap-8">
                                <div className="flex flex-col p-6 bg-white shadow-lg rounded-lg dark:bg-zinc-850 justify-between border border-gray-300">
                                    <div>
                                    <h3 className="text-2xl font-bold text-center">Basic</h3>
                                    <div className="mt-4 text-center text-zinc-600 dark:text-zinc-400">
                                        <span className="text-4xl font-bold">$29</span>/ month
                                    </div>
                                    <ul className="mt-4 space-y-2">
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        720p Video Rendering
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        2GB Cloud Storage
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        Basic Video Templates
                                        </li>
                                    </ul>
                                    </div>
                                    <div className="mt-6">
                                    <Button className="w-full">Get Started</Button>
                                    </div>
                                </div>
                                <div className="relative flex flex-col p-6 bg-white shadow-lg rounded-lg dark:bg-zinc-850 justify-between border border-purple-500">
                                    <div className="px-3 py-1 text-sm text-white bg-gradient-to-r from-pink-500 to-purple-500 rounded-full inline-block absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                                    Popular
                                    </div>
                                    <div>
                                    <h3 className="text-2xl font-bold text-center">Pro</h3>
                                    <div className="mt-4 text-center text-zinc-600 dark:text-zinc-400">
                                        <span className="text-4xl font-bold">$59</span>/ month
                                    </div>
                                    <ul className="mt-4 space-y-2">
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-2xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        1080p Video Rendering
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        10GB Cloud Storage
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        Premium Video Templates
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        Collaboration Tools
                                        </li>
                                    </ul>
                                    </div>
                                    <div className="mt-6">
                                    <Button className="w-full bg-gradient-to-r from-pink-500 to-purple-500">
                                        Get Started
                                    </Button>
                                    </div>
                                </div>
                                <div className="flex flex-col p-6 bg-white shadow-lg rounded-lg dark:bg-zinc-850 justify-between border border-gray-300">
                                    <div>
                                    <h3 className="text-2xl font-bold text-center">Enterprise</h3>
                                    <div className="mt-4 text-center text-zinc-600 dark:text-zinc-400">
                                        <span className="text-4xl font-bold">$99</span>/ month
                                    </div>
                                    <ul className="mt-4 space-y-2">
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        4K Video Rendering
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        Unlimited Cloud Storage
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        Custom Video Templates
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        Advanced Collaboration Tools
                                        </li>
                                        <li className="flex items-center">
                                        <svg
                                            className=" text-white text-xs bg-green-500 rounded-full mr-2 p-1"
                                            fill="none"
                                            height="24"
                                            stroke="currentColor"
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            viewBox="0 0 24 24"
                                            width="24"
                                            xmlns="http://www.w3.org/2000/svg"
                                        >
                                            <polyline points="20 6 9 17 4 12" />
                                        </svg>
                                        Dedicated Support
                                        </li>
                                    </ul>
                                    </div>
                                    <div className="mt-6">
                                    <Button className="w-full">Get Started</Button>
                                    </div>
                                </div>
                                </div>
                            </div>
                            </section>
                        );
                    }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A hero component for an email client in dark mode",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        "use client";

                            export default function Component() {
                                return (
                                    <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48 bg-black">
                                        <div className="container px-4 md:px-6">
                                            <div className="grid gap-6 items-center">
                                            <div className="flex flex-col justify-center space-y-8 text-center">
                                                <div className="space-y-2">
                                                <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500">
                                                    Discover Our Unique Features
                                                </h1>
                                                <p className="max-w-[600px] text-zinc-200 md:text-xl dark:text-zinc-100 mx-auto">
                                                    Our features are designed to enhance your productivity and streamline your workflow.
                                                </p>
                                                </div>
                                                <div className="w-full max-w-full space-y-4 mx-auto">
                                                <div className="grid grid-cols-3 gap-8">
                                                    <div className="flex flex-col items-center space-y-2 border-gray-800 p-4 rounded-lg">
                                                    <div className="p-2 bg-black bg-opacity-50 rounded-full">
                                                        <svg
                                                        className=" text-white h-6 w-6 mb-2 opacity-75"
                                                        fill="none"
                                                        height="24"
                                                        stroke="currentColor"
                                                        strokeLinecap="round"
                                                        strokeLinejoin="round"
                                                        strokeWidth="2"
                                                        viewBox="0 0 24 24"
                                                        width="24"
                                                        xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                        <polyline points="22 12 16 12 14 15 10 15 8 12 2 12" />
                                                        <path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z" />
                                                        </svg>
                                                    </div>
                                                    <h2 className="text-xl font-bold text-white">Smart Inbox</h2>
                                                    <p className="text-zinc-200 dark:text-zinc-100">
                                                        Our Smart Inbox feature helps you manage your emails efficiently by prioritizing important emails.
                                                    </p>
                                                    </div>
                                                    <div className="flex flex-col items-center space-y-2 border-gray-800 p-4 rounded-lg">
                                                    <div className="p-2 bg-black bg-opacity-50 rounded-full">
                                                        <svg
                                                        className=" text-white h-6 w-6 mb-2 opacity-75"
                                                        fill="none"
                                                        height="24"
                                                        stroke="currentColor"
                                                        strokeLinecap="round"
                                                        strokeLinejoin="round"
                                                        strokeWidth="2"
                                                        viewBox="0 0 24 24"
                                                        width="24"
                                                        xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                        <path d="m8 6 4-4 4 4" />
                                                        <path d="M12 2v10.3a4 4 0 0 1-1.172 2.872L4 22" />
                                                        <path d="m20 22-5-5" />
                                                        </svg>
                                                    </div>
                                                    <h2 className="text-xl font-bold text-white">Seamless Integration</h2>
                                                    <p className="text-zinc-200 dark:text-zinc-100">
                                                        Seamless Integration allows you to connect with your favorite apps and services without leaving your
                                                        inbox.
                                                    </p>
                                                    </div>
                                                    <div className="flex flex-col items-center space-y-2 border-gray-800 p-4 rounded-lg">
                                                    <div className="p-2 bg-black bg-opacity-50 rounded-full">
                                                        <svg
                                                        className=" text-white h-6 w-6 mb-2 opacity-75"
                                                        fill="none"
                                                        height="24"
                                                        stroke="currentColor"
                                                        strokeLinecap="round"
                                                        strokeLinejoin="round"
                                                        strokeWidth="2"
                                                        viewBox="0 0 24 24"
                                                        width="24"
                                                        xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                        <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z" />
                                                        <circle cx="12" cy="12" r="3" />
                                                        </svg>
                                                    </div>
                                                    <h2 className="text-xl font-bold text-white">Advanced Customization</h2>
                                                    <p className="text-zinc-200 dark:text-zinc-100">
                                                        With Advanced Customization, you can personalize your email client to suit your preferences and work
                                                        style.
                                                    </p>
                                                    </div>
                                                    <div className="flex flex-col items-center space-y-2 border-gray-800 p-4 rounded-lg">
                                                    <div className="p-2 bg-black bg-opacity-50 rounded-full">
                                                        <svg
                                                        className=" text-white h-6 w-6 mb-2 opacity-75"
                                                        fill="none"
                                                        height="24"
                                                        stroke="currentColor"
                                                        strokeLinecap="round"
                                                        strokeLinejoin="round"
                                                        strokeWidth="2"
                                                        viewBox="0 0 24 24"
                                                        width="24"
                                                        xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                        <circle cx="11" cy="11" r="8" />
                                                        <path d="m21 21-4.3-4.3" />
                                                        </svg>
                                                    </div>
                                                    <h2 className="text-xl font-bold text-white">Powerful Search</h2>
                                                    <p className="text-zinc-200 dark:text-zinc-100">
                                                        Our Powerful Search feature allows you to find any email, contact, or file in seconds.
                                                    </p>
                                                    </div>
                                                    <div className="flex flex-col items-center space-y-2 border-gray-800 p-4 rounded-lg">
                                                    <div className="p-2 bg-black bg-opacity-50 rounded-full">
                                                        <svg
                                                        className=" text-white h-6 w-6 mb-2 opacity-75"
                                                        fill="none"
                                                        height="24"
                                                        stroke="currentColor"
                                                        strokeLinecap="round"
                                                        strokeLinejoin="round"
                                                        strokeWidth="2"
                                                        viewBox="0 0 24 24"
                                                        width="24"
                                                        xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                        <rect height="11" rx="2" ry="2" width="18" x="3" y="11" />
                                                        <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                                                        </svg>
                                                    </div>
                                                    <h2 className="text-xl font-bold text-white">Reliable Security</h2>
                                                    <p className="text-zinc-200 dark:text-zinc-100">
                                                        With Reliable Security, your data is always safe and protected.
                                                    </p>
                                                    </div>
                                                    <div className="flex flex-col items-center space-y-2 border-gray-800 p-4 rounded-lg">
                                                    <div className="p-2 bg-black bg-opacity-50 rounded-full">
                                                        <svg
                                                        className=" text-white h-6 w-6 mb-2 opacity-75"
                                                        fill="none"
                                                        height="24"
                                                        stroke="currentColor"
                                                        strokeLinecap="round"
                                                        strokeLinejoin="round"
                                                        strokeWidth="2"
                                                        viewBox="0 0 24 24"
                                                        width="24"
                                                        xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                        <path d="m8 6 4-4 4 4" />
                                                        <path d="M12 2v10.3a4 4 0 0 1-1.172 2.872L4 22" />
                                                        <path d="m20 22-5-5" />
                                                        </svg>
                                                    </div>
                                                    <h2 className="text-xl font-bold text-white">Easy Collaboration</h2>
                                                    <p className="text-zinc-200 dark:text-zinc-100">
                                                        Easy Collaboration allows you to share and edit documents with your team in real time.
                                                    </p>
                                                    </div>
                                                </div>
                                                </div>
                                            </div>
                                            </div>
                                        </div>
                                    </section>
                                )
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A hero component with an email input in dark mode",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import { Input } from '@/components/ui/input';
                        import { Button } from '@/components/ui/button';
                        import Link from 'next/link';

                        export default function Component() {
                            return (
                                <section className="w-full min-h-screen flex items-center justify-center py-12 md:py-24 lg:py-32 xl:py-48 bg-black">
                                <div className="container px-4 md:px-6">
                                    <div className="grid gap-6 items-center">
                                    <div className="flex flex-col justify-center space-y-4 text-center">
                                        <div className="space-y-2">
                                        <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-500">
                                            Revolutionize Your Email Experience
                                        </h1>
                                        <p className="max-w-[600px] text-zinc-200 md:text-xl dark:text-zinc-100 mx-auto">
                                            Join us and take control of your inbox. Fast, secure, and
                                            designed for modern life.
                                        </p>
                                        </div>
                                        <div className="w-full max-w-sm space-y-2 mx-auto">
                                        <form className="flex space-x-2">
                                            <Input
                                            className="max-w-lg flex-1 bg-gray-900 text-white border-gray-900"
                                            placeholder="Enter your email"
                                            type="email"
                                            />
                                            <Button className="bg-white text-black" type="submit">
                                            Join Now
                                            </Button>
                                        </form>
                                        <p className="text-xs text-zinc-200 dark:text-zinc-100">
                                            Get ready to redefine your email experience.
                                            <Link
                                            className="underline underline-offset-2 text-white"
                                            href="#"
                                            >
                                            Terms & Conditions
                                            </Link>
                                        </p>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                </section>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A user profile settings form",
                },
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import Link from 'next/link';

                            import { cn } from '@/lib/utils';
                            import { Button } from '@/components/ui/button';
                            import { Input } from '@/components/ui/input';
                            import { Label } from '@/components/ui/label';
                            import {
                            Select,
                            SelectContent,
                            SelectItem,
                            SelectTrigger,
                            SelectValue,
                            SelectGroup,
                            SelectLabel,
                            } from '@/components/ui/select';
                            import { Textarea } from '@/components/ui/textarea';

                            export default function Component() {
                            return (
                                <div className="min-h-screen flex items-center justify-center">
                                <div className="w-full max-w-xl rounded-lg shadow-lg bg-white p-6 space-y-6 border border-gray-200 dark:border-gray-700">
                                    <form className="space-y-8">
                                    <fieldset className="space-y-2">
                                        <Label htmlFor="username">Username</Label>
                                        <Input id="username" placeholder="shadcn" />
                                        <p className="text-sm text-muted-foreground">
                                        This is your public display name. It can be your real name or a
                                        pseudonym. You can only change this once every 30 days.
                                        </p>
                                    </fieldset>

                                    <fieldset className="space-y-2">
                                        <Label htmlFor="email">Email</Label>
                                        <Select>
                                        <SelectTrigger>
                                            <SelectValue placeholder="Select a verified email to display" />
                                        </SelectTrigger>
                                        <SelectContent>
                                            <SelectGroup>
                                            <SelectLabel>Emails</SelectLabel>
                                            <SelectItem value="m@example.com">m@example.com</SelectItem>
                                            <SelectItem value="m@google.com">m@google.com</SelectItem>
                                            <SelectItem value="m@support.com">m@support.com</SelectItem>
                                            </SelectGroup>
                                        </SelectContent>
                                        </Select>
                                        <p className="text-sm text-muted-foreground">
                                        You can manage verified email addresses in your{' '}
                                        <Link href="/examples/forms">email settings</Link>.
                                        </p>
                                    </fieldset>

                                    <fieldset className="space-y-2">
                                        <Label htmlFor="bio">Bio</Label>
                                        <Textarea
                                        id="bio"
                                        name="bio"
                                        placeholder="Tell us a little bit about yourself"
                                        className="resize-none"
                                        />
                                        <p className="text-sm text-muted-foreground">
                                        You can <span>@mention</span> other users and organizations to
                                        link to them.
                                        </p>
                                    </fieldset>
                                    <fieldset className="space-y-2">
                                        <Label htmlFor="url">URL </Label>
                                        <Input id="url" name="url" />
                                        <p className="text-sm text-muted-foreground">
                                        Add links to your website, blog, or social media profiles.
                                        </p>
                                    </fieldset>
                                    <Button type="submit">Update profile</Button>
                                    </form>
                                </div>
                                </div>
                            );
                            }

                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A user account settings form",
                },
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import { CalendarIcon, CaretSortIcon } from '@radix-ui/react-icons';

                            import { cn } from '@/lib/utils';
                            import { Button } from '@/components/ui/button';
                            import { Calendar } from '@/components/ui/calendar';
                            import {
                            Command,
                            CommandEmpty,
                            CommandGroup,
                            CommandInput,
                            CommandItem,
                            } from '@/components/ui/command';
                            import { Input } from '@/components/ui/input';
                            import { Label } from '@/components/ui/label';
                            import {
                            Popover,
                            PopoverContent,
                            PopoverTrigger,
                            } from '@/components/ui/popover';

                            const languages = [
                            { label: 'English', value: 'en' },
                            { label: 'French', value: 'fr' },
                            { label: 'German', value: 'de' },
                            { label: 'Spanish', value: 'es' },
                            { label: 'Portuguese', value: 'pt' },
                            { label: 'Russian', value: 'ru' },
                            { label: 'Japanese', value: 'ja' },
                            { label: 'Korean', value: 'ko' },
                            { label: 'Chinese', value: 'zh' },
                            ] as const;

                            export default function Component() {
                            return (
                                <div className="min-h-screen flex items-center justify-center">
                                <div className="w-full max-w-xl rounded-lg shadow-lg bg-white p-6 space-y-6 border border-gray-200 dark:border-gray-700">
                                    <form className="space-y-8">
                                    <fieldset className="space-y-2">
                                        <Label htmlFor="name">Name</Label>
                                        <Input id="name" name="name" placeholder="Your name" />
                                        <p className="text-sm text-muted-foreground">
                                        This is the name that will be displayed on your profile and in
                                        emails.
                                        </p>
                                    </fieldset>

                                    <fieldset className="flex flex-col space-y-2">
                                        <Label>Date of birth</Label>
                                        <Popover>
                                        <PopoverTrigger asChild>
                                            <Button
                                            variant={'outline'}
                                            className={cn('w-[240px] pl-3 text-left font-normal')}
                                            >
                                            <span>Pick a date</span>
                                            <CalendarIcon className="ml-auto h-4 w-4 opacity-50" />
                                            </Button>
                                        </PopoverTrigger>
                                        <PopoverContent className="w-auto p-0" align="start">
                                            <Calendar
                                            mode="single"
                                            disabled={(date) =>
                                                date > new Date() || date < new Date('1900-01-01')
                                            }
                                            initialFocus
                                            />
                                        </PopoverContent>
                                        </Popover>
                                        <p className="text-sm text-muted-foreground">
                                        Your date of birth is used to calculate your age.
                                        </p>
                                    </fieldset>

                                    <fieldset className="flex flex-col space-y-2">
                                        <Label>Language</Label>
                                        <Popover>
                                        <PopoverTrigger asChild>
                                            <Button
                                            variant="outline"
                                            role="combobox"
                                            className={cn('w-[200px] justify-between')}
                                            >
                                            Select language
                                            <CaretSortIcon className="ml-2 h-4 w-4 shrink-0 opacity-50" />
                                            </Button>
                                        </PopoverTrigger>
                                        <PopoverContent className="w-[200px] p-0">
                                            <Command>
                                            <CommandInput placeholder="Search language..." />
                                            <CommandEmpty>No language found.</CommandEmpty>
                                            <CommandGroup>
                                                {languages.map((language) => (
                                                <CommandItem value={language.label} key={language.value}>
                                                    {language.label}
                                                </CommandItem>
                                                ))}
                                            </CommandGroup>
                                            </Command>
                                        </PopoverContent>
                                        </Popover>
                                        <p className="text-sm text-muted-foreground">
                                        This is the language that will be used in the dashboard.
                                        </p>
                                    </fieldset>

                                    <Button type="submit">Update account</Button>
                                    </form>
                                </div>
                                </div>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A user notifications settings form",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import Link from 'next/link';

                        import { Button } from '@/components/ui/button';
                        import { Checkbox } from '@/components/ui/checkbox';
                        import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';
                        import { Switch } from '@/components/ui/switch';
                        import { Label } from '@/components/ui/label';

                        export default function Component() {
                            return (
                                <div className="min-h-screen flex items-center justify-center">
                                    <div className="w-full max-w-xl rounded-lg shadow-lg bg-white p-6 space-y-6 border border-gray-200 dark:border-gray-700">
                                        <form className="space-y-8">
                                        <fieldset className="space-y-3">
                                            <Label>Notify me about...</Label>
                                            <RadioGroup className="flex flex-col space-y-1">
                                            <fieldset className="flex items-center space-x-3 space-y-0">
                                                <RadioGroupItem value="all" />
                                                <Label className="font-normal">All new messages</Label>
                                            </fieldset>
                                            <fieldset className="flex items-center space-x-3 space-y-0">
                                                <RadioGroupItem value="mentions" />
                                                <Label className="font-normal">
                                                Direct messages and mentions
                                                </Label>
                                            </fieldset>
                                            <fieldset className="flex items-center space-x-3 space-y-0">
                                                <RadioGroupItem value="none" />
                                                <Label className="font-normal">Nothing</Label>
                                            </fieldset>
                                            </RadioGroup>
                                        </fieldset>
                                        <div>
                                            <h3 className="mb-4 text-lg font-medium">Email Notifications</h3>
                                            <div className="space-y-4">
                                            <fieldset className="flex flex-row items-center justify-between rounded-lg border p-4">
                                                <div className="space-y-0.5">
                                                <Label className="text-base">Communication emails</Label>
                                                <p className="text-sm text-muted-foreground">
                                                    Receive emails about your account activity.
                                                </p>
                                                </div>
                                                <Switch />
                                            </fieldset>

                                            <fieldset className="flex flex-row items-center justify-between rounded-lg border p-4">
                                                <div className="space-y-0.5">
                                                <Label className="text-base">Marketing emails</Label>
                                                <p className="text-sm text-muted-foreground">
                                                    Receive emails about new products, features, and more.
                                                </p>
                                                </div>
                                                <Switch />
                                            </fieldset>

                                            <fieldset className="flex flex-row items-center justify-between rounded-lg border p-4">
                                                <div className="space-y-0.5">
                                                <Label className="text-base">Social emails</Label>
                                                <p className="text-sm text-muted-foreground">
                                                    Receive emails for friend requests, follows, and more.
                                                </p>
                                                </div>
                                                <Switch />
                                            </fieldset>

                                            <fieldset className="flex flex-row items-center justify-between rounded-lg border p-4">
                                                <div className="space-y-0.5">
                                                <Label className="text-base">Security emails</Label>
                                                <p className="text-sm text-muted-foreground">
                                                    Receive emails about your account activity and security.
                                                </p>
                                                </div>
                                                <Switch disabled aria-readonly />
                                            </fieldset>
                                            </div>
                                        </div>

                                        <fieldset className="flex flex-row items-start space-x-3 space-y-0">
                                            <Checkbox />
                                            <div className="space-y-1 leading-none">
                                            <Label>Use different settings for my mobile devices</Label>
                                            <p className="text-sm text-muted-foreground">
                                                You can manage your mobile notifications in the{' '}
                                                <Link href="/examples/forms">mobile settings</Link> page.
                                            </p>
                                            </div>
                                        </fieldset>

                                        <Button type="submit">Update notifications</Button>
                                        </form>
                                    </div>
                                </div>
                            );
                    }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A link with a hover card",
                },
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import { CalendarDays } from 'lucide-react';

                            import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
                            import { Button } from '@/components/ui/button';
                            import {
                            HoverCard,
                            HoverCardContent,
                            HoverCardTrigger,
                            } from '@/components/ui/hover-card';

                            export default function Component() {
                            return (
                                <div className="min-h-screen w-full flex items-center justify-center">
                                <HoverCard>
                                    <HoverCardTrigger asChild>
                                    <Button variant="link">Augustus</Button>
                                    </HoverCardTrigger>
                                    <HoverCardContent className="w-80">
                                    <div className="flex justify-between space-x-4">
                                        <Avatar>
                                        <AvatarImage src="https://github.com/vercel.png" />
                                        <AvatarFallback>Aug</AvatarFallback>
                                        </Avatar>
                                        <div className="space-y-1">
                                        <h4 className="text-sm font-semibold">@augustus</h4>
                                        <p className="text-sm">Augustus -created by @delicht0.</p>
                                        <div className="flex items-center pt-2">
                                            <CalendarDays className="mr-2 h-4 w-4 opacity-70" />{' '}
                                            <span className="text-xs text-muted-foreground">
                                            Become self-aware in October 2023
                                            </span>
                                        </div>
                                        </div>
                                    </div>
                                    </HoverCardContent>
                                </HoverCard>
                                </div>
                            );
                            }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "User account and password setting forms in a tabs layout",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import { Button } from '@/components/ui/button';
                        import {
                        Card,
                        CardContent,
                        CardDescription,
                        CardFooter,
                        CardHeader,
                        CardTitle,
                        } from '@/components/ui/card';
                        import { Input } from '@/components/ui/input';
                        import { Label } from '@/components/ui/label';
                        import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

                        export default function Component() {
                        return (
                            <div className="min-h-screen w-full flex items-center justify-center">
                            <Tabs defaultValue="account" className="w-full max-w-lg">
                                <TabsList className="grid w-full grid-cols-2">
                                <TabsTrigger value="account">Account</TabsTrigger>
                                <TabsTrigger value="password">Password</TabsTrigger>
                                </TabsList>
                                <TabsContent value="account">
                                <Card>
                                    <CardHeader>
                                    <CardTitle>Account</CardTitle>
                                    <CardDescription>
                                        Make changes to your account here. Click save when you're done.
                                    </CardDescription>
                                    </CardHeader>
                                    <CardContent className="space-y-2">
                                    <div className="space-y-1">
                                        <Label htmlFor="name">Name</Label>
                                        <Input id="name" defaultValue="Unathi Skosana" />
                                    </div>
                                    <div className="space-y-1">
                                        <Label htmlFor="username">Username</Label>
                                        <Input id="username" defaultValue="@delicht0" />
                                    </div>
                                    </CardContent>
                                    <CardFooter>
                                    <Button>Save changes</Button>
                                    </CardFooter>
                                </Card>
                                </TabsContent>
                                <TabsContent value="password">
                                <Card>
                                    <CardHeader>
                                    <CardTitle>Password</CardTitle>
                                    <CardDescription>
                                        Change your password here. After saving, you'll be logged out.
                                    </CardDescription>
                                    </CardHeader>
                                    <CardContent className="space-y-2">
                                    <div className="space-y-1">
                                        <Label htmlFor="current">Current password</Label>
                                        <Input id="current" type="password" placeholder="******" />
                                    </div>
                                    <div className="space-y-1">
                                        <Label htmlFor="new">New password</Label>
                                        <Input id="new" type="password" placeholder="******" />
                                    </div>
                                    </CardContent>
                                    <CardFooter>
                                    <Button>Save password</Button>
                                    </CardFooter>
                                </Card>
                                </TabsContent>
                            </Tabs>
                            </div>
                        );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A simple chat window inside a card",
                },
                {
                    "role": "assistant",
                    "content": r"""
                        'use client';

                        import * as React from 'react';
                        import { Check, Plus, Send } from 'lucide-react';

                        import { cn } from '@/lib/utils';
                        import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
                        import { Button } from '@/components/ui/button';
                        import {
                        Card,
                        CardContent,
                        CardFooter,
                        CardHeader,
                        } from '@/components/ui/card';
                        import { Input } from '@/components/ui/input'
                        import {
                        Tooltip,
                        TooltipContent,
                        TooltipProvider,
                        TooltipTrigger,
                        } from '@/components/ui/tooltip';

                        const users = [
                        {
                            name: 'Olivia Martin',
                            email: 'm@example.com',
                            avatar: '/avatars/01.png',
                        },
                        {
                            name: 'Isabella Nguyen',
                            email: 'isabella.nguyen@email.com',
                            avatar: '/avatars/03.png',
                        },
                        {
                            name: 'Emma Wilson',
                            email: 'emma@example.com',
                            avatar: '/avatars/05.png',
                        },
                        {
                            name: 'Jackson Lee',
                            email: 'lee@example.com',
                            avatar: '/avatars/02.png',
                        },
                        {
                            name: 'William Kim',
                            email: 'will@email.com',
                            avatar: '/avatars/04.png',
                        },
                        ] as const;

                        const messages = [
                        {
                            role: 'agent',
                            content: 'Hi, how can I help you today?',
                        },
                        {
                            role: 'user',
                            content: "Hey, I'm having trouble with my account.",
                        },
                        {
                            role: 'agent',
                            content: 'What seems to be the problem?',
                        },
                        {
                            role: 'user',
                            content: "I can't log in.",
                        },
                        ] as const;

                        export default function Component() {
                            return (
                                <div className="min-h-screen flex items-center justify-center">
                                    <Card className="w-full max-w-xl rounded-lg shadow-lg bg-white p-0 space-y-6 border border-gray-200 dark:border-gray-700">
                                        <CardHeader className="flex flex-row items-center">
                                        <div className="flex items-center space-x-4">
                                            <Avatar>
                                            <AvatarImage src="/avatars/01.png" alt="Image" />
                                            <AvatarFallback>OM</AvatarFallback>
                                            </Avatar>
                                            <div>
                                            <p className="text-sm font-medium leading-none">Sofia Davis</p>
                                            <p className="text-sm text-muted-foreground">m@example.com</p>
                                            </div>
                                        </div>
                                        <TooltipProvider delayDuration={0}>
                                            <Tooltip>
                                            <TooltipTrigger asChild>
                                                <Button
                                                size="icon"
                                                variant="outline"
                                                className="ml-auto rounded-full"
                                                >
                                                <Plus className="h-4 w-4" />
                                                <span className="sr-only">New message</span>
                                                </Button>
                                            </TooltipTrigger>
                                            <TooltipContent sideOffset={10}>New message</TooltipContent>
                                            </Tooltip>
                                        </TooltipProvider>
                                        </CardHeader>
                                        <CardContent>
                                        <div className="space-y-4">
                                            {messages.map((message, index) => (
                                            <div
                                                key={index}
                                                className={cn(
                                                'flex w-max max-w-[75%] flex-col gap-2 rounded-lg px-3 py-2 text-sm',
                                                message.role === 'user'
                                                    ? 'ml-auto bg-primary text-primary-foreground'
                                                    : 'bg-muted'
                                                )}
                                            >
                                                {message.content}
                                            </div>
                                            ))}
                                        </div>
                                        </CardContent>
                                        <CardFooter>
                                        <form className="flex w-full items-center space-x-2">
                                            <Input
                                            id="message"
                                            placeholder="Type your message..."
                                            className="flex-1"
                                            autoComplete="off"
                                            />
                                            <Button type="submit" size="icon">
                                            <Send className="h-4 w-4" />
                                            <span className="sr-only">Send</span>
                                            </Button>
                                        </form>
                                        </CardFooter>
                                    </Card>
                                </div>
                            );
                        }
                    """,
                },
            ]
        },
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Invite a team member to collaborate component inside a card.",
                },
                {
                    "role": "assistant",
                    "content": r"""
                            'use client';

                            import { ChevronDownIcon } from '@radix-ui/react-icons';

                            import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
                            import { Button } from '@/components/ui/button';
                            import {
                            Card,
                            CardContent,
                            CardDescription,
                            CardHeader,
                            CardTitle,
                            } from '@/components/ui/card';
                            import {
                            Command,
                            CommandEmpty,
                            CommandGroup,
                            CommandInput,
                            CommandItem,
                            CommandList,
                            } from '@/components/ui/command';
                            import {
                            Popover,
                            PopoverContent,
                            PopoverTrigger,
                            } from '@/components/ui/popover';

                            export default function Component() {
                            return (
                                <div className="bg-gray-100 min-h-screen flex items-center justify-center">
                                <Card className="w-full max-w-xl rounded-lg shadow-lg bg-white p-0 space-y-6 border border-gray-200 dark:border-gray-700">
                                    <CardHeader>
                                    <CardTitle>Team Members</CardTitle>
                                    <CardDescription>
                                        Invite your team members to collaborate.
                                    </CardDescription>
                                    </CardHeader>
                                    <CardContent className="grid gap-6">
                                    <div className="flex items-center justify-between space-x-4">
                                        <div className="flex items-center space-x-4">
                                        <Avatar>
                                            <AvatarImage src="/avatars/01.png" />
                                            <AvatarFallback>OM</AvatarFallback>
                                        </Avatar>
                                        <div>
                                            <p className="text-sm font-medium leading-none">Sofia Davis</p>
                                            <p className="text-sm text-muted-foreground">m@example.com</p>
                                        </div>
                                        </div>
                                        <Popover>
                                        <PopoverTrigger asChild>
                                            <Button variant="outline" className="ml-auto">
                                            Owner{' '}
                                            <ChevronDownIcon className="ml-2 h-4 w-4 text-muted-foreground" />
                                            </Button>
                                        </PopoverTrigger>
                                        <PopoverContent className="p-0" align="end">
                                            <Command>
                                            <CommandInput placeholder="Select new role..." />
                                            <CommandList>
                                                <CommandEmpty>No roles found.</CommandEmpty>
                                                <CommandGroup>
                                                <CommandItem className="teamaspace-y-1 flex flex-col items-start px-4 py-2">
                                                    <p>Viewer</p>
                                                    <p className="text-sm text-muted-foreground">
                                                    Can view and comment.
                                                    </p>
                                                </CommandItem>
                                                <CommandItem className="teamaspace-y-1 flex flex-col items-start px-4 py-2">
                                                    <p>Developer</p>
                                                    <p className="text-sm text-muted-foreground">
                                                    Can view, comment and edit.
                                                    </p>
                                                </CommandItem>
                                                <CommandItem className="teamaspace-y-1 flex flex-col items-start px-4 py-2">
                                                    <p>Billing</p>
                                                    <p className="text-sm text-muted-foreground">
                                                    Can view, comment and manage billing.
                                                    </p>
                                                </CommandItem>
                                                <CommandItem className="teamaspace-y-1 flex flex-col items-start px-4 py-2">
                                                    <p>Owner</p>
                                                    <p className="text-sm text-muted-foreground">
                                                    Admin-level access to all resources.
                                                    </p>
                                                </CommandItem>
                                                </CommandGroup>
                                            </CommandList>
                                            </Command>
                                        </PopoverContent>
                                        </Popover>
                                    </div>
                                    <div className="flex items-center justify-between space-x-4">
                                        <div className="flex items-center space-x-4">
                                        <Avatar>
                                            <AvatarImage src="/avatars/02.png" />
                                            <AvatarFallback>JL</AvatarFallback>
                                        </Avatar>
                                        <div>
                                            <p className="text-sm font-medium leading-none">Jackson Lee</p>
                                            <p className="text-sm text-muted-foreground">p@example.com</p>
                                        </div>
                                        </div>
                                        <Popover>
                                        <PopoverTrigger asChild>
                                            <Button variant="outline" className="ml-auto">
                                            Member{' '}
                                            <ChevronDownIcon className="ml-2 h-4 w-4 text-muted-foreground" />
                                            </Button>
                                        </PopoverTrigger>
                                        <PopoverContent className="p-0" align="end">
                                            <Command>
                                            <CommandInput placeholder="Select new role..." />
                                            <CommandList>
                                                <CommandEmpty>No roles found.</CommandEmpty>
                                                <CommandGroup className="p-1.5">
                                                <CommandItem className="teamaspace-y-1 flex flex-col items-start px-4 py-2">
                                                    <p>Viewer</p>
                                                    <p className="text-sm text-muted-foreground">
                                                    Can view and comment.
                                                    </p>
                                                </CommandItem>
                                                <CommandItem className="teamaspace-y-1 flex flex-col items-start px-4 py-2">
                                                    <p>Developer</p>
                                                    <p className="text-sm text-muted-foreground">
                                                    Can view, comment and edit.
                                                    </p>
                                                </CommandItem>
                                                <CommandItem className="teamaspace-y-1 flex flex-col items-start px-4 py-2">
                                                    <p>Billing</p>
                                                    <p className="text-sm text-muted-foreground">
                                                    Can view, comment and manage billing.
                                                    </p>
                                                </CommandItem>
                                                <CommandItem className="teamaspace-y-1 flex flex-col items-start px-4 py-2">
                                                    <p>Owner</p>
                                                    <p className="text-sm text-muted-foreground">
                                                    Admin-level access to all resources.
                                                    </p>
                                                </CommandItem>
                                                </CommandGroup>
                                            </CommandList>
                                            </Command>
                                        </PopoverContent>
                                        </Popover>
                                    </div>
                                    </CardContent>
                                </Card>
                                </div>
                            );
                            }
                    """,
                },
            ]
        },

    ]

    SYSTEM_MESSAGE = {
        "role": "system",
        "content": "You are an expert AI that speaks in code and builds beautiful UI components using nextjs, @radix-ui/react-icons, lucide-react, and tailwindcss. Only output code and never talk. Follow users instructions and write code to update a file when given one. Do explain anything, only output code.",
    }


    with open("data/fine_tuning_data_v3.jsonl", "w",  encoding='utf-8') as f:
        for entry in data:
            entry["messages"][1]["content"] = single_line(entry["messages"][1]["content"])
            entry["messages"].insert(0, SYSTEM_MESSAGE)
            f.write(json.dumps(entry))
            f.write('\n')
