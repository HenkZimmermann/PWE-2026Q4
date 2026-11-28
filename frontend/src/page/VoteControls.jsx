import { useEffect, useState } from "react";
import { getThreadVote, setThreadVote } from "../api/votes";
import "./VoteControls.css";

export default function VoteControls({label, threadId}) {
    const isThread = threadId !== undefined;
    const [vote, setVote] = useState(isThread ? null : {score: 0, ownVote: 0});

    useEffect(() => {
        if (!isThread)
            return;

        let active = true;
        getThreadVote(threadId)
            .then((result) => {
                if (active)
                    setVote(result);
            })
            .catch((error) => console.error(error));

        return () => {
            active = false;
        };
    }, [isThread, threadId]);

    async function toggleVote(direction) {
        const nextVote = vote.ownVote === direction ? 0 : direction;
        if (!isThread) {
            setVote({score: nextVote, ownVote: nextVote});
            return;
        }

        try {
            setVote(await setThreadVote(threadId, nextVote));
        } catch (error) {
            console.error(error)
        }
    }

    return (
        <>
            <div className="vote-controls" role="group" aria-label={label}>
                <button type="button" aria-label="Upvote" aria-pressed={vote?.ownVote === 1} disabled={!vote} onClick={() => toggleVote(1)}>
                    ↑
                </button>
                <output aria-label="Votes">{vote?.score ?? "–"}</output>
                <button type="button" aria-label="Downvote" aria-pressed={vote?.ownVote === -1} disabled={!vote} onClick={() => toggleVote(-1)}>
                    ↓
                </button>
            </div>
        </>
    );
}
