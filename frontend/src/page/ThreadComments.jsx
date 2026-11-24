import { useEffect, useState } from "react";
import { createComment, getThreadComments } from "../api/comments";
import "./ThreadComments.css";

// TODO Selben Demo User wie im Dashboard verwenden
const demoUserId = 2;

// Komponente für Kommentarspalte, lädt Daten selber aus Backend für gegebene Thread ID
export default function ThreadComments({threadId, onCommentCreated}) {
    const [comments, setComments] = useState(null);
    const [message, setMessage] = useState("");
    const [loadError, setLoadError] = useState("");
    const [reload, setReload] = useState(0);

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
            await createComment({threadId, message: text, userId: demoUserId});
            setMessage("");
            setReload((value) => value + 1);
            onCommentCreated(threadId);
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <section className="thread-comments">
            <h2>Kommentare</h2>

            <form className="thread-comment-form" onSubmit={handleSubmit}>
                <label htmlFor="comment-message">Kommentar schreiben</label>
                <textarea id="comment-message" rows={3} value={message} onChange={(event) => setMessage(event.target.value)} required />
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
                    <p>{comment.content}</p>
                </article>
            ))}
        </section>
    );
}
