import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getUserStatistics } from "../api/user_statistics.js";
import "./UserStatistics.css";

const fullDate = new Intl.DateTimeFormat("de-DE", {
    day: "numeric",
    month: "long",
    year: "numeric",
});

const shortDate = new Intl.DateTimeFormat("de-DE", {
    day: "2-digit",
    month: "2-digit",
});

export default function ProfileStats({ userId }) {
    const [stats, setStats] = useState(null);
    const [error, setError] = useState("");

    useEffect(() => {
        let active = true;

        async function loadStats() {
            setStats(null);
            setError("");

            try {
                const data = await getUserStatistics(userId);
                if (active) setStats(data);
            } catch (err) {
                if (active) {
                    setError(
                        err instanceof Error
                            ? err.message
                            : "Statistiken konnten nicht geladen werden."
                    );
                }
            }
        }

        loadStats();

        return () => {
            active = false;
        };
    }, [userId]);

    if (error) return <p role="alert">{error}</p>;
    if (!stats) return <p role="status">Statistiken werden geladen …</p>;

    const metrics = [
        { label: "Threads", value: stats.thread_count },
        { label: "Kommentare", value: stats.comment_count },
        { label: "Votes auf meine Threads", value: stats.thread_votes_received },
        { label: "Follower", value: stats.follower_count },
    ];

    const weeks = stats.weekly_activity;
    // Die aktivste Woche bestimmt die Höhe eines vollen Balkens
    const maxPosts = Math.max(0, ...weeks.map(week => week.threads + week.comments));

    return (
        <div className="profile-stats">
            <p className="profile-stats-joined">
                Mitglied seit {fullDate.format(new Date(stats.joined_at))}
            </p>
            {/* Gesamtzahlen seit der Registrierung */}
            <dl className="profile-stats-metrics">
                {metrics.map(({ label, value }) => (
                    <div key={label}>
                        <dt>{label}</dt>
                        <dd>{value}</dd>
                    </div>
                ))}
            </dl>

            <section className="profile-stats-activity">
                {/* User spezifische Aktivitäts Anzeige */}
                <h3>Meine Aktivität</h3>

                {maxPosts === 0 ? (
                    <p>In den letzten acht Wochen hast du keine Beiträge veröffentlicht.</p>
                ) : (
                    <>
                        <div className="profile-stats-chart">
                            {weeks.map(week => {
                                const date = new Date(`${week.week_start}T00:00:00`);
                                const summary =
                                    "Woche ab ${fullDate.format(date)}: " +
                                    week.threads +" Threads,"+ week.comments+" Kommentare";

                                return (
                                    <div
                                        key={week.week_start}
                                        className="profile-stats-week"
                                        role="img"
                                        aria-label={summary}
                                        title={summary}
                                    >
                                        <div className="profile-stats-bar">
                                            <span
                                                className="profile-stats-bar-threads"
                                                style={{ height: week.threads / maxPosts * 100 }}
                                            />
                                            <span
                                                className="profile-stats-bar-comments"
                                                style={{ height: week.comments / maxPosts * 100 }}
                                            />
                                        </div>
                                        <small>{shortDate.format(date)}</small>
                                    </div>
                                );
                            })}
                        </div>

                        <p className="profile-stats-legend">
                            <span>Threads</span>
                            <span>Kommentare</span>
                        </p>
                    </>
                )}
            </section>
            {/* Gruppen Statistiken */}
            <section className="profile-stats-groups">
                <h3>Meine Gruppen</h3>
                {stats.groups.length > 0 ? (
                    <ul>
                        {stats.groups.map(group => (
                            <li key={group.id}>{group.name}</li>
                        ))}
                    </ul>
                ) : (
                    <p>Du bist noch keiner Gruppe beigetreten.</p>
                )}
            </section>

            <section className="profile-stats-latest">
                <h3>Letzter Thread</h3>
                {/* Weiterleitung auf den neusten Thread */}
                {stats.latest_thread ? (
                    <>
                        <Link to={`/threads/${stats.latest_thread.id}`}>
                            {stats.latest_thread.title}
                        </Link>
                        <p>{fullDate.format(new Date(stats.latest_thread.created_at))}</p>
                    </>
                ) : (
                    <p>Du hast noch keinen Thread erstellt.</p>
                )}
            </section>
        </div>
    );
}