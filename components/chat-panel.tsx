import { useEffect, useState } from 'react';
import { type UseChatHelpers } from 'ai/react'

import { Checkbox } from '@/components/ui/checkbox'
import { Button } from '@/components/ui/button'
import { PromptForm } from '@/components/prompt-form'
import { IconRefresh, IconStop } from '@/components/ui/icons'
import { FileSelector } from '@/components/file-selector'

export interface ChatPanelProps
    extends Pick<
        UseChatHelpers,
        | 'append'
        | 'isLoading'
        | 'reload'
        | 'messages'
        | 'stop'
        | 'input'
        | 'setInput'
    > {
    id?: string
    VM: any
    currentFile: any
    setCurrentFile: any
}

export function ChatPanel({
    id,
    isLoading,
    stop,
    append,
    reload,
    input,
    setInput,
    messages,
    VM,
    currentFile,
    setCurrentFile
}: ChatPanelProps) {

    const [includeFile, setIncludeFile] = useState(true);
    const [fileList, setFileList] = useState([]);

    useEffect(() => {
        async function fetchFiles() {
            if (!VM) {
                console.error('SDK VM is not available');
                return;
            }
            const files = await VM.getFsSnapshot();
            setFileList(Object.keys(files));
        }
        fetchFiles();
    }, [VM]);

    async function getFileContent(fileName: string) {
        if (!VM) {
            console.error('SDK VM is not available');
            return;
        }

        const files = await VM.getFsSnapshot();
        return files ? files[fileName] : '';
    }

    async function getCurrentViewedFile() {
        return await getFileContent(currentFile);
    }


    return (
        <div className="fixed inset-x-0 bottom-0 right-[50%]">
            <div className="mx-auto sm:max-w-2xl sm:px-4">
                <div className="flex h-10 items-center justify-center">
                    {isLoading ? (
                        <Button
                            variant="outline"
                            onClick={() => stop()}
                            className="bg-background"
                        >
                            <IconStop className="mr-2" />
                            Stop generating
                        </Button>
                    ) : (
                        messages?.length > 0 && (
                            <Button
                                variant="outline"
                                onClick={() => reload()}
                                className="bg-background"
                            >
                                <IconRefresh className="mr-2" />
                                Regenerate response
                            </Button>
                        )
                    )}
                </div>
                <div className="space-y-4 border-t bg-background px-4 py-2 shadow-lg sm:rounded-t-xl sm:border md:py-4">
                    <div className="flex items-center justify-between">
                        <FileSelector fileList={fileList} onSelectFile={setCurrentFile} />
                        <div className="flex items-center space-x-2">
                            <Checkbox checked={includeFile} onCheckedChange={(value) => setIncludeFile(value)} id="include" />
                            <label
                                htmlFor="include"
                                className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                            >
                                Include file in instructions
                            </label>
                        </div>
                    </div>


                    <PromptForm
                        onSubmit={async value => {
                            const fileContent = await getCurrentViewedFile();
                            const content = includeFile ? `Instructions: ${value}\nFile: ${fileContent}` : `Instructions: ${value}`

                            await append({
                                id,
                                content,
                                role: 'user'
                            })
                        }}
                        input={input}
                        setInput={setInput}
                        isLoading={isLoading}
                    />
                </div>
            </div>
        </div>
    )
}
