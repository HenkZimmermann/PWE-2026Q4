import { useEffect, useRef, useState } from "react";
import { apiBaseUrl } from "../api/config";
import "./ConnectionMonitor.css";

// Verbindung testen
async function serverAvailable(url, isHealthy) {
    try {
        const response = await fetch(url, {
            cache: "no-store", // Wichtig nicht cachen, sonst ist der Check sinnlos
            signal: AbortSignal.timeout(4000),
        });
        return response.ok && await isHealthy(response);
    } catch {
        return false;
    }
}

export default function ConnectionMonitor() {
    const [disconnected, setDisconnected] = useState(false);
    const dialogRef = useRef(null);

    useEffect(() => {
        let active = true;
        let timer;
        let failures = 0;

        // Beide Server verbindungen testen
        async function checkConnection() {
            const [frontend, backend] = await Promise.all([
                // Frontend erreichbar?
                serverAvailable(import.meta.env.BASE_URL + "health.txt",
                    async (response) => (await response.text()).trim() === "pwe-frontend-ok"),
                
                // Backend erreichbar?
                serverAvailable(apiBaseUrl + "/health",
                    async (response) => (await response.json()).status === "ok"),
            ]);

            if (!active)
                return;

            if (frontend && backend) {
                if (failures >= 2) {
                    window.location.reload();
                    return;
                }

                failures = 0;
            } else {
                failures += 1;
                if (failures >= 2)
                    setDisconnected(true);
            }

            timer = window.setTimeout(checkConnection, 5000);
        }

        checkConnection();
        return () => {
            active = false;
            window.clearTimeout(timer);
        };
    }, []);

    // Dialog anzeigen wenn Verbindung fehlschlägt
    useEffect(() => {
        if (disconnected)
            dialogRef.current.showModal();
    }, [disconnected]);

    if (!disconnected)
        return null;

    return (
        <dialog className="connection-dialog" ref={dialogRef}
            aria-labelledby="connection-dialog-title"
            aria-describedby="connection-dialog-description"
            onCancel={(event) => event.preventDefault()}
        >
            <h2 id="connection-dialog-title">Server derzeit nicht erreichbar</h2>
            <p id="connection-dialog-description">Sobald die Verbindung wieder da ist, lädt diese Seite automatisch neu.</p>
        </dialog>
    );
}
