import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { getGroups } from "../../api/groups";
import { createThread, getThreadFeed } from "../../api/threads";
import CreateThreadDialog from "../../page/CreateThreadDialog";
import FloatingActionButton from "../../page/FloatingActionButton";
import ThreadCard from "../../page/ThreadCard";
import "./DashboardSection.css";

// TODO Gibt ja noch keinen Login, daher Hard-coded
const demoUserId = 2;

// Wieviele Threads mehr sollen pro Ladevorgang abgerufen werden
const feedStep = 10;

// Die letzten Anzeigen merken. Dadurch können wir beim zurückkehren wieder auf die Scrollposition zurück
const dashboardHistory = new Map();

function Element() {
    const {key} = useLocation();
    const [threads, setThreads] = useState(null);
    const [groups, setGroups] = useState([]);
    
    const [hasMore, setHasMore] = useState(false);    
    const [feedRequest, setFeedRequest] = useState(() => dashboardHistory.get(key) ?? {limit: feedStep, groupId: ""});

    const [showCreateForm, setShowCreateForm] = useState(false);

    // Den Feed aus dem Backend laden (ggf. live via Button)
    useEffect(() => {
        let active = true;
        getThreadFeed(feedRequest.limit, feedRequest.groupId)
            .then((page) => {
                if (active) {
                    setThreads(page.threads);
                    setHasMore(page.hasMore);
                }
            })
            .catch((error) => {
                if (active)
                    console.error(error);
            });
        return () => {
            active = false;
        };
    }, [feedRequest]);

    // Erst scrollen, wenn der Feed wieder geladen hat
    useEffect(() => {
        if (threads && feedRequest.scrollY !== undefined)
            window.scrollTo(0, feedRequest.scrollY);
    }, [threads, feedRequest]);

    // Scroll Position merken wenn wir einen Thread öffnen
    function rememberDashboard() {
        dashboardHistory.set(key, {
            limit: threads.length,
            groupId: feedRequest.groupId,
            scrollY: window.scrollY
        });
    }

    // Callback für den Button
    function loadMoreThreads() {
        setFeedRequest({limit: threads.length + feedStep, groupId: feedRequest.groupId});
    }

    // Callback für Wechsel von Gruppen Filter
    function changeGroup(event) {
        setThreads(null);
        setHasMore(false);
        setFeedRequest({limit: feedStep, groupId: event.target.value});
    }

    // Gruppen laden aus Backend
    useEffect(() => {
        getGroups()
            .then(setGroups)
            .catch((error) => console.error(error));
    }, []);

    // Neuen Thread ans Backend geben wenn abgeschickt
    async function handleCreate({title, content, groupId}) {
        await createThread({title, content, groupId, userId: demoUserId});
        setHasMore(false);
        setFeedRequest((request) => ({limit: feedStep, groupId: request.groupId}));
    }

    return (
        <div className="dashboard">
            <h1>Dashboard</h1>
            {/* Thread anlegen Dialog, nur bedingt zeigen */}
            {showCreateForm && (
                <CreateThreadDialog groups={groups} onCreate={handleCreate} onClose={() => setShowCreateForm(false)}/>
            )}

            {/* Gruppen Filter */}
            <label className="dashboard-group-filter">
                Gruppe
                <select value={feedRequest.groupId} onChange={changeGroup}>
                    <option value="">Alle Gruppen</option>
                    {groups.map((group) => (
                        <option key={group.id} value={group.id}>{group.name}</option>
                    ))}
                </select>
            </label>

            {/* Keine Threads? Nachricht anzeigen */}
            {threads?.length === 0 && (
                <div className="dashboard-empty-feed" role="status">
                    <strong>Es gibt noch keine Beiträge</strong>
                    <p>Über + kannst du den ersten erstellen.</p>
                </div>
            )}

            {/* Geladene Threads aus Backend anzeigen */}
            {threads?.map((thread) => (
                <ThreadCard key={thread.id} thread={thread} preview onOpen={rememberDashboard} />
            ))}

            {/* Mehr Threads laden */}
            {hasMore && (
                <button className="dashboard-load-more" type="button" onClick={loadMoreThreads}>Weitere Beiträge laden</button>
            )}

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
