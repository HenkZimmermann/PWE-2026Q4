import { useEffect, useState } from "react";
import { getGroups } from "../../api/groups";
import { createThread, getThreadFeed } from "../../api/threads";
import CreateThreadDialog from "../../page/CreateThreadDialog";
import FloatingActionButton from "../../page/FloatingActionButton";
import ThreadCard from "../../page/ThreadCard";
import "./DashboardSection.css";

const demoUserId = 2; // TODO Gibt ja noch keinen Login, daher Hard-coded

function Element() {
    const [threads, setThreads] = useState(null);
    const [groups, setGroups] = useState([]);
    const [feedVersion, setFeedVersion] = useState(0);
    const [showCreateForm, setShowCreateForm] = useState(false);

    // Den Feed aus dem Backend laden
    useEffect(() => {
        const controller = new AbortController();
        getThreadFeed(controller.signal)
            .then(setThreads)
            .catch((error) => {
                if (!controller.signal.aborted)
                    console.error(error);
            });
        return () => controller.abort();
    }, [feedVersion]);

    // Gruppen laden aus Backend
    useEffect(() => {
        getGroups()
            .then(setGroups)
            .catch((error) => console.error(error));
    }, []);

    // Neuen Thread ans Backend geben wenn abgeschickt
    async function handleCreate({title, content, groupId}) {
        await createThread({ title, content, groupId, userId: demoUserId });
        setFeedVersion((version) => version + 1);
    }

    return (
        <div>
            <h1>Dashboard</h1>
            
            {/* Thread anlegen Dialog, nur bedingt zeigen */}
            {showCreateForm && (
                <CreateThreadDialog groups={groups} onCreate={handleCreate} onClose={() => setShowCreateForm(false)}/>
            )}

            {/* Keine Threads? Nachricht anzeigen */}
            {threads?.length === 0 && (
                <div className="dashboard-empty-feed" role="status">
                    <strong>Es gibt noch keine Beiträge.</strong>
                    <p>Über + kannst du den ersten erstellen.</p>
                </div>
            )}

            {/* Geladene Threads aus Backend anzeigen */}
            {threads?.map((thread) => (
                <ThreadCard key={thread.id} thread={thread} />
            ))}

            {/* Button zum Thread anlegen Dialog öffnen */}
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
    element: <Element />
};

export default DashboardSection;
