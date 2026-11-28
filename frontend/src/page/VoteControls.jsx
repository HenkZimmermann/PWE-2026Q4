import { useEffect, useState } from "react";
import { getVote, setVote } from "../api/votes";
import "./VoteControls.css";

export default function VoteControls({label, path}) {
    const [vote, setVoteState] = useState(null);

    useEffect(() => {
        let active = true;
        getVote(path)
            .then((result) => {
                if (active)
                    setVoteState(result);
            })
            .catch((error) => console.error(error));

        return () => {
            active = false;
        };
    }, [path]);

    async function toggleVote(direction) {
        const nextVote = vote.ownVote === direction ? 0 : direction;

        try {
            setVoteState(await setVote(path, nextVote));
        } catch (error) {
            console.error(error);
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
