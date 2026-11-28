import { Link } from "react-router-dom";
import { fromMarkdown } from "mdast-util-from-markdown";
import MarkdownContent from "./MarkdownContent";
import VoteControls from "./VoteControls";
import "./ThreadCard.css";

const blockContainers = new Set(["root", "blockquote", "list", "listItem"]);

function readText(node) {
    if (node.type === "text" || node.type === "inlineCode" || node.type === "code")
        return node.value;

    if (node.type === "break")
        return " ";

    return node.children?.map(readText).join(blockContainers.has(node.type) ? " " : "") ?? "";
}

function markdownToPlainText(markdown) {
    return readText(fromMarkdown(markdown)).replace(/\s+/gu, " ").trim();
}

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
    
    const plainText = preview ? markdownToPlainText(thread.content) : "";
    const matchIndex = pattern ? plainText.search(pattern) : -1;
    const showContent = matchIndex !== -1;
    let content = plainText;

    // Content zuschneiden wenn preview und Suchergebnis im Content
    if (showContent) {
        // 60 zeichen vor und 100 Zeichen nach dem Treffer den text zeigen
        const start = Math.max(0, matchIndex - 60);
        const end = matchIndex + searchTerm.length + 100;
        content = plainText.slice(start, end);
        
        // ... wenn was abgeschnitten wurde
        if (start > 0)
            content = "..." + content;

        if (end < plainText.length)
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
            {preview ? (
                <p className={!showContent ? "thread-card-preview" : undefined}>
                    {highlightMatches(content, pattern)}
                </p>
            ) : (
                <MarkdownContent>{thread.content}</MarkdownContent>
            )}

            <footer className="thread-card-stats">
                <VoteControls key={thread.id} label="Beitrag bewerten" />
                <span>{thread.commentCount} Kommentare</span>
            </footer>
        </article>
    );
}
