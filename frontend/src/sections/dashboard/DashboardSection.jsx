import FloatingActionButton from "../../page/FloatingActionButton";
import "./DashboardSection.css";

const exampleThread = {
    title: "Wieso ist dieses Forum so unfassbar toll?",
    content: "Ich arbeite mit meinem guten Kollegen Henk an diesem Forum und es ist fantastisch. Einfach besser als jedes Forum würde ich sagen.",
    groupName: "Global",
    authorName: "Tim",
    publishedAt: "2026-11-18",
    commentCount: 4
};

function ThreadCard({ thread }) {
    return (
        <article className="dashboard-thread">
            <header className="dashboard-thread-meta">
                <strong>{thread.groupName}</strong>
                <span>von {thread.authorName}</span>
                <time dateTime={thread.publishedAt}>{thread.publishedAt}</time>
            </header>
            <h2>{thread.title}</h2>
            <p>{thread.content}</p>
            <footer className="dashboard-thread-stats">
                <span>{thread.commentCount} Kommentare</span>
            </footer>
        </article>
    );
}

function Element() {
    const handleCreate = () => {
        alert("Neu"); // TODO, beispiel alert
    };

    return (
        <div>
            <h1>Dashboard</h1>
            <ThreadCard thread={exampleThread} />
            <FloatingActionButton onClick={handleCreate} content="+" />
        </div>
    );
}

export const DashboardSection = {
    title: "Dashboard",
    icon: "🖥️",
    url: "/",
    subUrls: [
        /*{
        url: "...",
        element: <... />
        }*/
    ],
    showInSidebar: true,
    element: <Element />,
};

export default DashboardSection;
