import { useEffect, useState } from "react";
import { useLocation, useSearchParams } from "react-router-dom";
import { getGroups } from "../../api/groups";
import { searchThreads } from "../../api/threads";
import ThreadCard from "../../page/ThreadCard";
import "./SearchSection.css";

// Wieviele Threads mehr sollen pro Ladevorgang abgerufen werden
const pageSize = 10;

function Element() {
    const {key} = useLocation();
    const [params, setParams] = useSearchParams();
    const [groups, setGroups] = useState([]);

    // Gruppen laden aus Backend
    useEffect(() => {
        getGroups()
            .then(setGroups)
            .catch((error) => console.error(error));
    }, []);

    return (
        <Search key={key} searchTerm={(params.get("q") || "").trim()} searchGroupId={params.get("group_id") || ""} groups={groups} onSearch={setParams}/>
    );
}

function Search({searchTerm, searchGroupId, groups, onSearch}) {
    const [term, setTerm] = useState(searchTerm);
    const [groupId, setGroupId] = useState(searchGroupId);
    const [threads, setThreads] = useState(null);
    const [hasMore, setHasMore] = useState(false);
    const [request, setRequest] = useState({limit: pageSize});

    // Suche aus der URL laden, z.B. wenn wir über Bookmark oder "zurück" auf die Seite kommen
    // Parameter werden aus übergeordnetem Element() übergeben
    useEffect(() => {
        if (!searchTerm)
            return;

        searchThreads(searchTerm, searchGroupId, request.limit)
            .then((page) => {
                setThreads(page.threads);
                setHasMore(page.hasMore);
            })
            .catch((error) => console.error(error));
    }, [searchTerm, searchGroupId, request]);

    // Callback für den Button
    function handleSearch(event) {
        event.preventDefault();

        // Haben wir überhaupt Inhalt in der Query?
        const query = term.trim();
        if (!query)
            return;

        const params = {q: query};
        if (groupId)
            params.group_id = groupId;
        onSearch(params);
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
                <ThreadCard key={thread.id} thread={thread} preview searchTerm={searchTerm} />
            ))}

            {/* Mehr Threads laden */}
            {hasMore && (
                <button type="button" onClick={() => setRequest({limit: threads.length + pageSize})}>Weitere Beiträge laden</button>
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
