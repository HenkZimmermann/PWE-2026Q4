import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getThreadById } from "../api/threads";
import ThreadCard from "./ThreadCard";
import ThreadComments from "./ThreadComments";
import "./ThreadDetail.css";

export default function ThreadDetail() {
    const {threadId} = useParams();
    const [thread, setThread] = useState(null);

    useEffect(() => {
        let active = true;
        setThread(null);

        getThreadById(threadId)
            .then((thread) => {
                if (active)
                    setThread(thread);
            })
            .catch((error) => console.error(error));

        return () => {
            active = false;
        };
    }, [threadId]);

    return (
        <div className="thread-detail">
            {thread === null ? (
                <p role="status">Beitrag nicht gefunden.</p>
            ) : (
                <>
                    <ThreadCard thread={thread} />
                    <ThreadComments key={thread.id} threadId={thread.id} />
                </>
            )}
        </div>
    );
}
