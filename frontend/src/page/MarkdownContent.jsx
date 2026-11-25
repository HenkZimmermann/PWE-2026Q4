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
