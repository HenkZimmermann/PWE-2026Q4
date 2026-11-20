import { useEffect, useState } from "react";
import { getGroups } from "../../api/groups";
import { searchThreads } from "../../api/threads";
import ThreadCard from "../../page/ThreadCard";
import "./SearchSection.css";

// Wieviele Threads mehr sollen pro Ladevorgang abgerufen werden
const pageSize = 10;

function Element() {
    const [term, setTerm] = useState("");
    const [groupId, setGroupId] = useState("");
    const [groups, setGroups] = useState([]);
    const [search, setSearch] = useState(null);
    const [threads, setThreads] = useState(null);
    const [hasMore, setHasMore] = useState(false);

    // Gruppen laden aus Backend
    useEffect(() => {
        getGroups()
            .then(setGroups)
            .catch((error) => console.error(error));
    }, []);

    // Suche laden
    async function loadResults(request) {
        try {
            const page = await searchThreads(request.term, request.groupId, pageSize);
            setThreads(() => page.threads);
            setHasMore(page.hasMore);
        } catch (error) {
            console.error(error);
        }
    }

    // Callback für den Button
    function handleSearch(event) {
        event.preventDefault();

        const request = {term: term.trim(), groupId};
        setSearch(request);
        setThreads(null);
        setHasMore(false);
        loadResults(request);
    }

    return (
        <div className="search-section">
            <h1>Suche</h1>
            <form className="search-form" onSubmit={handleSearch}>
                <label>
                    Suchbegriff
                    <input type="search" value={term} onChange={(event) => setTerm(event.target.value)} required/>
                </label>

                {/* Gruppen Filter */}
                <label>
                    Gruppe
                    <select value={groupId} onChange={(event) => setGroupId(event.target.value)}>
                        <option value="">Alle Gruppen</option>
                        {groups.map((group) => (
                            <option key={group.id} value={group.id}>{group.name}</option>
                        ))}
                    </select>
                </label>
                <button type="submit">Suchen</button>
            </form>

            {/* Keine Threads? Nachricht anzeigen */}
            {threads?.length === 0 && <p role="status">Keine Beiträge gefunden.</p>}

            {/* Geladene Threads aus Backend anzeigen */}
            {threads?.map((thread) => (
                <ThreadCard key={thread.id} thread={thread} preview searchTerm={search.term} />
            ))}

            {/* Mehr Threads laden */}
            {hasMore && (
                <button type="button" disabled={loading} onClick={() => loadResults(search, threads.length)}>Weitere Beiträge laden</button>
            )}
        </div>
    );
}

export const SearchSection = {
    title: "Suche",
    icon: "🔎",
    url: "/search",
    subUrls: [
        /*{
        url: "...",
        element: <... />
        }*/
    ],
    showInSidebar: true,
    element: <Element />,
};

export default SearchSection;
