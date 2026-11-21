import { useEffect, useState } from "react";
import { getThreadComments } from "../api/comments";
import "./ThreadComments.css";

// Komponente für Kommentarspalte, lädt Daten selber aus Backend für gegebene Thread ID
export default function ThreadComments({threadId}) {
    const [comments, setComments] = useState(null);

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
    }, [threadId]);

    return (
        <section className="thread-comments">
            <h2>Kommentare</h2>

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
