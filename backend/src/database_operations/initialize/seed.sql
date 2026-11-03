INSERT INTO Roles (role_id, name, permissions) VALUES
(1, 'Admin', ARRAY[
    'users.manage',
    'roles.manage',
    'groups.manage',
    'threads.delete',
    'comments.delete'
]),
(2, 'Moderator', ARRAY[
    'threads.delete',
    'comments.delete',
    'groups.manage'
]),
(3, 'User', ARRAY[
    'threads.create',
    'comments.create',
    'threads.vote',
    'comments.vote'
])
ON CONFLICT DO NOTHING;

INSERT INTO Users (
    user_id, username, email, password_hash, role_id
) VALUES
(1, 'admin', 'admin@example.com', 'DEMO_HASH_ADMIN', 1),
(2, 'max_mustermann', 'max@example.com', 'DEMO_HASH_MAX', 3),
(3, 'lisa_dev', 'lisa@example.com', 'DEMO_HASH_LISA', 3),
(4, 'tom_gaming', 'tom@example.com', 'DEMO_HASH_TOM', 3),
(5, 'anna_mod', 'anna@example.com', 'DEMO_HASH_ANNA', 2),
(6, 'sarah_design', 'sarah@example.com', 'DEMO_HASH_SARAH', 3),
(7, 'ben_python', 'ben@example.com', 'DEMO_HASH_BEN', 3),
(8, 'mia_student', 'mia@example.com', 'DEMO_HASH_MIA', 3)
ON CONFLICT DO NOTHING;


INSERT INTO Groups (
    group_id, group_name, category, members,
    system_created, description
) VALUES
(1, 'Python Community', 'Programmierung', 120, TRUE,
 'Fragen, Tipps und Projekte rund um Python.'),

(2, 'Web Development', 'Technologie', 85, TRUE,
 'Frontend, Backend, APIs und moderne Webtechnologien.'),

(3, 'Gaming Lounge', 'Gaming', 210, FALSE,
 'Spieleempfehlungen, Gaming-News und Diskussionen.'),

(4, 'University Life', 'Studium', 64, FALSE,
 'Lerntipps, Prüfungen und Erfahrungen aus dem Studium.'),

(5, 'Design & UX', 'Kreativität', 47, FALSE,
 'UI-Design, Prototypen und User Experience.'),

(6, 'Hardware & Homelab', 'Technologie', 93, FALSE,
 'Server, Netzwerke, Container und Hardware.')
ON CONFLICT DO NOTHING;

INSERT INTO Threads (
    thread_id, created_at, message,
    user_id, votes, group_id, title
) VALUES
(1, '2026-10-20 09:30:00',
 'Ich lerne gerade Python. Welche Projekte eignen sich für den Einstieg?',
 2, 15, 1, 'Gute Python-Projekte für Anfänger'),

(2, '2026-10-21 14:15:00',
 'Ich suche ein Framework für meine erste REST-API. Was würdet ihr empfehlen?',
 3, 8, 2, 'Welches Webframework ist empfehlenswert?'),

(3, '2026-10-22 18:45:00',
 'Was spielt ihr aktuell am liebsten? Ich suche etwas Neues für den Feierabend.',
 4, 22, 3, 'Spieleempfehlungen für den Herbst'),

(4, '2026-10-23 11:00:00',
 'Wie organisiert ihr euch während der Prüfungsphase?',
 8, 12, 4, 'Tipps für eine stressfreie Prüfungsphase'),

(5, '2026-10-24 16:20:00',
 'Ich möchte meine erste API entwickeln. Worauf sollte ich besonders achten?',
 2, 19, 2, 'Die erste REST-API entwickeln'),

(6, '2026-10-25 13:10:00',
 'Welche kostenlosen Tools verwendet ihr für UI-Prototypen?',
 6, 7, 5, 'Kostenlose Tools für UI-Design'),

(7, '2026-10-26 20:00:00',
 'Welche Vorteile haben Docker-Container gegenüber virtuellen Maschinen?',
 7, 11, 6, 'Docker oder virtuelle Maschinen?'),

(8, '2026-10-27 08:50:00',
 'Habt ihr Empfehlungen für gute Lernressourcen zu Datenbanken?',
 4, 5, 4, 'Datenbanken verständlich lernen'),

(9, '2026-10-27 15:40:00',
 'Ich habe Probleme mit verschachtelten Kommentaren in meiner Datenbank.',
 3, 6, 2, 'Wie speichert man Kommentar-Antworten?'),

(10, '2026-10-28 10:15:00',
 'Was sollte ein gutes Community-Forum unbedingt bieten?',
 5, 9, 5, 'Features für eine moderne Community')
ON CONFLICT DO NOTHING;

INSERT INTO Comments (
    comment_id, thread_id, parent_comment_id,
    message, votes, user_id, created_at
) VALUES

(1, 1, NULL,
 'Ein To-do-Programm ist ein guter Einstieg. Danach kannst du eine kleine API bauen.',
 6, 3, '2026-10-20 10:00:00'),

(2, 1, 1,
 'Danke! Ich werde zuerst das To-do-Programm ausprobieren.',
 2, 2, '2026-10-20 10:15:00'),

(3, 1, NULL,
 'Ich würde zusätzlich ein kleines Web-Scraping-Projekt empfehlen.',
 4, 7, '2026-10-20 11:30:00'),

(4, 2, NULL,
 'Für Python würde ich FastAPI empfehlen. Die automatische API-Dokumentation ist super.',
 9, 2, '2026-10-21 15:00:00'),

(5, 2, 4,
 'Sehe ich auch so. Gerade für REST-APIs ist FastAPI sehr angenehm.',
 3, 3, '2026-10-21 15:30:00'),

(6, 2, 4,
 'Django ist auch eine gute Wahl, wenn man viele Funktionen direkt mitbringen möchte.',
 5, 7, '2026-10-21 16:00:00'),

(7, 3, NULL,
 'Ich spiele aktuell Baldur’s Gate 3 und kann es sehr empfehlen.',
 7, 6, '2026-10-22 19:00:00'),

(8, 3, NULL,
 'Wenn du etwas mit Freunden suchst, probiere ein Koop-Spiel aus.',
 4, 4, '2026-10-22 19:20:00'),

(9, 4, NULL,
 'Ich plane jeden Tag drei Lernblöcke und mache dazwischen Pausen.',
 8, 2, '2026-10-23 12:00:00'),

(10, 4, 9,
 'Die Pomodoro-Technik hilft mir auch, konzentriert zu bleiben.',
 3, 8, '2026-10-23 12:20:00'),

(11, 4, 10,
 'Ich nutze zusätzlich Karteikarten für Definitionen und Fachbegriffe.',
 2, 5, '2026-10-23 12:45:00'),

(12, 5, NULL,
 'Achte auf passende HTTP-Statuscodes, Validierung und eine klare Struktur.',
 10, 5, '2026-10-24 17:00:00'),

(13, 5, 12,
 'Und vergiss nicht, Fehlerfälle und Berechtigungen zu testen.',
 5, 3, '2026-10-24 17:15:00'),

(14, 6, NULL,
 'Figma ist für Prototypen und erste UI-Entwürfe sehr praktisch.',
 6, 2, '2026-10-25 14:00:00'),

(15, 6, 14,
 'Für einfache Wireframes kann man auch Penpot ausprobieren.',
 3, 6, '2026-10-25 14:30:00'),

(16, 7, NULL,
 'Container sind ressourcenschonend, weil sie den Kernel des Hosts teilen.',
 8, 3, '2026-10-26 20:30:00'),

(17, 7, 16,
 'VMs sind dafür praktisch, wenn man unterschiedliche Betriebssysteme benötigt.',
 4, 7, '2026-10-26 20:45:00'),

(18, 8, NULL,
 'Die PostgreSQL-Dokumentation ist ein guter Startpunkt.',
 5, 5, '2026-10-27 09:00:00'),

(19, 9, NULL,
 'Du kannst parent_comment_id als Fremdschlüssel auf comment_id verwenden.',
 7, 7, '2026-10-27 16:00:00'),

(20, 9, 19,
 'Genau so ist es bei mir umgesetzt. NULL bedeutet, dass es ein Hauptkommentar ist.',
 3, 3, '2026-10-27 16:20:00'),

(21, 9, 20,
 'Für die Anzeige musst du die Antworten dann rekursiv oder über mehrere Abfragen laden.',
 4, 2, '2026-10-27 16:45:00'),

(22, 10, NULL,
 'Eine gute Suche und sinnvolle Kategorien sind meiner Meinung nach besonders wichtig.',
 6, 6, '2026-10-28 11:00:00'),

(23, 10, 22,
 'Ich würde außerdem Benachrichtigungen für Antworten einbauen.',
 4, 5, '2026-10-28 11:20:00')

ON CONFLICT DO NOTHING;


SELECT setval(
    pg_get_serial_sequence('roles', 'role_id'),
    (SELECT MAX(role_id) FROM Roles)
);

SELECT setval(
    pg_get_serial_sequence('users', 'user_id'),
    (SELECT MAX(user_id) FROM Users)
);

SELECT setval(
    pg_get_serial_sequence('groups', 'group_id'),
    (SELECT MAX(group_id) FROM Groups)
);

SELECT setval(
    pg_get_serial_sequence('threads', 'thread_id'),
    (SELECT MAX(thread_id) FROM Threads)
);

SELECT setval(
    pg_get_serial_sequence('comments', 'comment_id'),
    (SELECT MAX(comment_id) FROM Comments)
);

INSERT INTO votes (user_id, thread_id) VALUES
(2, 1),
(3, 1),
(7, 1),
(2, 2),
(5, 2),
(6, 3),
(2, 3),
(3, 3),
(8, 4),
(2, 4),
(5, 5),
(7, 5),
(3, 5),
(2, 6),
(6, 6),
(3, 7),
(7, 7),
(2, 7),
(5, 8),
(8, 8),
(7, 9),
(2, 9),
(6, 10),
(5, 10)
ON CONFLICT DO NOTHING;


INSERT INTO member_of (user_id, group_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(2, 4),
(3, 1),
(3, 2),
(3, 5),
(4, 3),
(4, 6),
(5, 1),
(5, 2),
(5, 4),
(5, 5),
(6, 4),
(6, 5),
(6, 2),
(7, 1),
(7, 2),
(7, 6),
(8, 4),
(8, 1)
ON CONFLICT DO NOTHING;


INSERT INTO follows (user_id, followed_user_id) VALUES
(2, 3),
(2, 5),
(2, 7),
(3, 2),
(3, 7),
(3, 6),
(4, 6),
(4, 7),
(5, 2),
(5, 3),
(5, 6),
(6, 3),
(6, 5),
(7, 2),
(7, 3),
(7, 5),
(8, 2),
(8, 5)
ON CONFLICT DO NOTHING;
