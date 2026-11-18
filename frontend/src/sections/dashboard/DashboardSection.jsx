import { useEffect, useState } from "react";
import CreateThreadDialog from "../../page/CreateThreadDialog";
import FloatingActionButton from "../../page/FloatingActionButton";
import "./DashboardSection.css";

const apiBaseUrl = "http://localhost:8000";

function ThreadCard({ thread }) {
    return (
        <article className="dashboard-thread">
            <header className="dashboard-thread-meta">
                <strong>{thread.groupName}</strong>
                <span>von {thread.authorName}</span>
                {thread.publishedAt && (
                    <time dateTime={thread.publishedAt}>{thread.publishedAt.slice(0, 10)}</time>
                )}
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
    const [threads, setThreads] = useState([]);
    const [localThreads, setLocalThreads] = useState([]);
    const [showCreateForm, setShowCreateForm] = useState(false);

    useEffect(() => {
        fetch(apiBaseUrl + "/threads/feed")
            .then((response) => {
                if (!response.ok)
                    throw new Error("Feed konnte nicht geladen werden.");
                return response.json();
            })
            .then(setThreads)
            .catch((error) => console.error(error));
    }, []);

    function handleCreate({ title, content, groupName }) {
        const publishedAt = new Date().toLocaleDateString("sv-SE");
        setLocalThreads((currentThreads) => [
            {
                id: `local-${currentThreads.length + 1}`,
                title,
                content,
                groupName,
                authorName: "Tim",
                publishedAt,
                commentCount: 0
            },
            ...currentThreads,
        ]);
    }

    const feed = [...localThreads, ...threads];

    return (
        <div>
            <h1>Dashboard</h1>
            {showCreateForm && (
                <CreateThreadDialog groups={["Global"]} onCreate={handleCreate} onClose={() => setShowCreateForm(false)}/>
            )}

            {feed.map((thread) => (
                <ThreadCard key={thread.id} thread={thread} />
            ))}

            <FloatingActionButton onClick={() => setShowCreateForm(true)} content="+" />
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
