import Markdown from "react-markdown";
import "./MarkdownContent.css";

// Die Komponente render Markdown 
// TODO Noch keine Bilder, dafür haben wir noch nicht die Infrastruktur
export default function MarkdownContent({children}) {
    return (
        <div className="markdown-content">
            <Markdown skipHtml disallowedElements={["img"]}>{children}</Markdown>
        </div>
    );
}

// Markdown Hinweis, der an den Textfeldern angezeigt werden kann, dass sie Markdown unterstützen
export function MarkdownHint({id}) {
    return (
        <small id={id}>
            Markdown möglich, z. B. <code>**fett**</code>, <code>- Listenpunkt</code> oder <code>{"`Code`"}</code>.
        </small>
    );
}
