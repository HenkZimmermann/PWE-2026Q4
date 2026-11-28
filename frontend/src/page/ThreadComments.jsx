import { useEffect, useState } from "react";
import { createComment, deleteComment, editComment, getThreadComments } from "../api/comments";
import { useUser } from "../context/UserProvider";
import MarkdownContent, { MarkdownHint } from "./MarkdownContent";
import VoteControls from "./VoteControls";
import "./ThreadComments.css";

// Komponente für Kommentarspalte, lädt Daten selber aus Backend für gegebene Thread ID
export default function ThreadComments({threadId, onCommentCreated, onCommentDeleted}) {
    const {user} = useUser();
    const [comments, setComments] = useState(null);
    const [message, setMessage] = useState("");
    const [reload, setReload] = useState(0);
    const [editingId, setEditingId] = useState(null);

    // Thread Kommentare laden
    useEffect(() => {
        let active = true;
        getThreadComments(threadId)
            .then((comments) => {
                if (active)
                    setComments(comments);
            })
            .catch((error) => console.error(error));

        return () => {
            active = false;
        };
    }, [threadId, reload]);

    // Abschicken
    async function handleSubmit(event) {
        event.preventDefault();
        const text = message.trim();

        try {
            await createComment({threadId, message: text, userId: user.id});
            setMessage("");
            setReload((value) => value + 1);
            onCommentCreated(threadId);
        } catch (error) {
            console.error(error);
        }
    }

    async function handleEdit(event, commentId) {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const content = formData.get("message");
        if (!content.trim())
            return;

        try {
            await editComment(commentId, content);
            setComments((current) => current.map((comment) =>
                comment.id === commentId ? {...comment, content} : comment
            ));
            setEditingId((current) => current === commentId ? null : current);
        } catch (error) {
            console.error(error);
        }
    }

    async function handleDelete(commentId) {
        if (!window.confirm("Diesen Kommentar löschen? Vorhandene Antworten bleiben erhalten."))
            return;

        try {
            const {removed} = await deleteComment(commentId);
            if (removed)
                onCommentDeleted(threadId);
            setReload((value) => value + 1);
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <section className="thread-comments">
            <h2>Kommentare</h2>

            <form className="thread-comment-form" onSubmit={handleSubmit}>
                <label htmlFor="comment-message">Kommentar schreiben</label>
                <textarea id="comment-message" rows={3} value={message} onChange={(event) => setMessage(event.target.value)} aria-describedby="comment-markdown-hint" required />
                <MarkdownHint id="comment-markdown-hint" />
                <button type="submit" disabled={!message.trim()}>Kommentar senden</button>
            </form>

            {/* Keine Kommentare? Nachricht*/}
            {comments?.length === 0 && <p>Es gibt noch keine Kommentare.</p>}

            {/* Kommentare auflisten*/}
            {comments?.map((comment) => (
                <article className="thread-comment" key={comment.id}>
                    <header>
                        <strong>{comment.authorName}</strong>
                        {comment.publishedAt && (
                            <time dateTime={comment.publishedAt}>{comment.publishedAt.slice(0, 10)}</time>
                        )}
                    </header>
                    {editingId === comment.id && !comment.deleted ? (
                        <form className="thread-comment-form thread-comment-edit-form" onSubmit={(event) => handleEdit(event, comment.id)}>
                            <label htmlFor={`edit-comment-${comment.id}`}>Kommentar bearbeiten</label>
                            <textarea id={`edit-comment-${comment.id}`} name="message" rows={3} defaultValue={comment.content} aria-describedby="edit-comment-markdown-hint" required autoFocus />
                            <MarkdownHint id="edit-comment-markdown-hint" />
                            <div className="thread-comment-edit-actions">
                                <button type="button" onClick={() => setEditingId(null)}>Abbrechen</button>
                                <button type="submit">Speichern</button>
                            </div>
                        </form>
                    ) : (
                        <MarkdownContent>{comment.content}</MarkdownContent>
                    )}
                    {!comment.deleted && (
                        <footer>
                            <VoteControls path={`/comments/${comment.id}/vote`} label="Kommentar bewerten" />
                            {editingId !== comment.id && (user.id === comment.authorId || user.role === "Admin") && (
                                <div className="thread-comment-actions">
                                    <button type="button" onClick={() => setEditingId(comment.id)}>Bearbeiten</button>
                                    <button type="button" onClick={() => handleDelete(comment.id)}>Löschen</button>
                                </div>
                            )}
                        </footer>
                    )}
                </article>
            ))}
        </section>
    );
}
