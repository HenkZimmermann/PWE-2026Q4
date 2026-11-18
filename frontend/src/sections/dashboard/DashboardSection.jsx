import { useEffect, useState } from "react";
import CreateThreadDialog from "../../page/CreateThreadDialog";
import FloatingActionButton from "../../page/FloatingActionButton";
import ThreadCard from "../../page/ThreadCard";

const apiBaseUrl = "http://localhost:8000"; // TODO sollten wir noch auslagern irgendwie zentral, in env?
const demoUserId = 2; // TODO Gibt ja noch keinen Login, daher Hard-coded

function Element() {
    const [threads, setThreads] = useState([]);
    const [groups, setGroups] = useState([]);
    const [feedVersion, setFeedVersion] = useState(0);
    const [showCreateForm, setShowCreateForm] = useState(false);

    // Den Feed aus dem backend laden
    useEffect(() => {
        const controller = new AbortController();
        fetch(apiBaseUrl + "/threads/feed", {signal: controller.signal})
            .then((response) => {
                if (!response.ok)
                    throw new Error("Feed konnte nicht geladen werden.");
                return response.json();
            })
            .then(setThreads)
            .catch((error) => {
                if (!controller.signal.aborted)
                    console.error(error);
            });
        return () => controller.abort();
    }, [feedVersion]);

    // Gruppen laden für den Thread Erstellen Dialog
    // Machen wir hier und nicht zentral grade, weil wir ja ggf. dn Dialog aus einer Gruppe später aufrufen
    // Da wollen wir dann natürlich nur die jewielige Gruppe zur Auswahl haben
    useEffect(() => {
        fetch(apiBaseUrl + "/groups/all")
            .then((response) => response.json())
            .then((data) => {
                if (Array.isArray(data))
                    setGroups(data.map(([id, name]) => ({id, name})));
            })
            .catch((error) => console.error(error));
    }, []);

    // Neuen Thread ans backend geben
    async function handleCreate({title, content, groupId}) {
        const response = await fetch(apiBaseUrl + "/threads/create", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                title,
                message: content,
                group_id: groupId,
                user_id: demoUserId,
            })
        });
        if (!response.ok)
            throw new Error("Beitrag konnte nicht gespeichert werden.");
        setFeedVersion((version) => version + 1);
    }

    return (
        <div>
            <h1>Dashboard</h1>
            {showCreateForm && (
                <CreateThreadDialog groups={groups} onCreate={handleCreate} onClose={() => setShowCreateForm(false)}/>
            )}

            {threads.map((thread) => (
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
