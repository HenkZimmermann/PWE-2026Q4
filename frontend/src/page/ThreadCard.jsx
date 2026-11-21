import { Link } from "react-router-dom";
import "./ThreadCard.css";

function highlightMatches(text, pattern) {
    if (!pattern)
        return text;

    // Durch die Klammern liefert split abwechselnd normalen Text und Treffer
    return text.split(pattern).map((part, index) => (
        index % 2 === 1 ? <mark key={index}>{part}</mark> : part
    ));
}

export default function ThreadCard({thread, preview = false, searchTerm = "", onOpen}) {
    // Sonderzeichen als normalen Text suchen, nicht als Regex interpretieren
    const escapedTerm = searchTerm.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const pattern = escapedTerm ? new RegExp("(" + escapedTerm + ")", "iu") : null;
    
    const matchIndex = pattern ? thread.content.search(pattern) : -1;
    const showExcerpt = preview && matchIndex !== -1;
    let content = thread.content;

    // Content zuschneiden wenn preview und Suchergebnis im Content
    if (showExcerpt) {
        // 60 zeichen vor und 100 Zeichen nach dem Treffer den text zeigen
        const start = Math.max(0, matchIndex - 60);
        const end = matchIndex + searchTerm.length + 100;
        content = thread.content.slice(start, end);
        
        // ... wenn was abgeschnitten wurde
        if (start > 0)
            content = "..." + content;

        if (end < thread.content.length)
            content += "...";
    }

    const title = highlightMatches(thread.title, pattern);

    return (
        <article className="thread-card">

            {/* Gruppe, Author und Datum */}
            <header className="thread-card-meta">
                <strong>{thread.groupName}</strong>
                <span>von {thread.authorName}</span>
                {thread.publishedAt && (
                    <time dateTime={thread.publishedAt}>{thread.publishedAt.slice(0, 10)}</time>
                )}
            </header>

            {/* Titel und Inhalt. Titel als Link, wenn die Card eine Preview ist */}
            <h2>
                {preview ? <Link to={"/threads/" + thread.id} onClick={onOpen}>{title}</Link> : title}
            </h2>
            <p className={preview && !showExcerpt ? "thread-card-preview" : undefined}>
                {highlightMatches(content, pattern)}
            </p>

            {/* Statistik wie Anzahl Kommentare und mehr später */}
            <footer className="thread-card-stats">
                <span>{thread.commentCount} Kommentare</span>
            </footer>
        </article>
    );
}
