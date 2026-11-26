import { createContext, useContext, useState } from "react";

const UserContext = createContext(null);
// Dient als Zwischenspeicherung der notwendigen Userinfos (Username, email, Rolle)
// Kann von allen weiteren JSX Dateien einfach abgefragt werden
export function UserProvider({ children }) {
    const [user, setUser] = useState();

    return (
        <UserContext.Provider value={{ user, setUser }}>
            {children}
        </UserContext.Provider>
    );
}

export function useUser() {
    return useContext(UserContext);
}