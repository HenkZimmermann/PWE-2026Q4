import { useEffect, useRef, useState } from "react";
import { MarkdownHint } from "./MarkdownContent";
import "./CreateThreadDialog.css";

export default function EditThreadDialog({thread, onSave, onClose}) {
    const dialogRef = useRef(null);

    useEffect(() => {
        dialogRef.current.showModal();
    }, []);

    async function handleSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const title = formData.get("title").trim();
        const content = formData.get("content");

        if (!title || !content.trim())
            return;

        try {
            await onSave({title, content});
            dialogRef.current?.close();
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <dialog
            ref={dialogRef}
            className="create-thread-dialog"
            aria-label="Beitrag bearbeiten"
            onClose={onClose}
            onCancel={(event) => {
                event.preventDefault();
            }}
        >
            <form onSubmit={handleSubmit}>
                <h2>Beitrag bearbeiten</h2>
                <label>
                    Titel
                    <input name="title" defaultValue={thread.title} maxLength={255} required autoFocus />
                </label>
                <div className="create-thread-dialog-content">
                    <label htmlFor="edit-thread-content">Text</label>
                    <textarea id="edit-thread-content" name="content" rows={5} defaultValue={thread.content} aria-describedby="edit-thread-markdown-hint" required />
                    <MarkdownHint id="edit-thread-markdown-hint" />
                </div>
                <div className="create-thread-dialog-actions">
                    <button type="button" onClick={() => dialogRef.current.close()}>Abbrechen</button>
                    <button type="submit">Speichern</button>
                </div>
            </form>
        </dialog>
    );
}
