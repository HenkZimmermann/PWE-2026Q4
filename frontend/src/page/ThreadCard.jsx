import "./ThreadCard.css";

export default function ThreadCard({thread, preview = false}) {
    return (
        <article className="thread-card">
            <header className="thread-card-meta">
                <strong>{thread.groupName}</strong>
                <span>von {thread.authorName}</span>
                {thread.publishedAt && (
                    <time dateTime={thread.publishedAt}>{thread.publishedAt.slice(0, 10)}</time>
                )}
            </header>
            <h2>{thread.title}</h2>
            <p className={preview ? "thread-card-preview" : undefined}>{thread.content}</p>
            <footer className="thread-card-stats">
                <span>{thread.commentCount} Kommentare</span>
            </footer>
        </article>
    );
}
