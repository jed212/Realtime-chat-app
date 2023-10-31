import React, { useEffect } from "react";
import { useState } from "react"
import Navigate from "../Components/Navigate";


const withAuthentication = (wrappedComponent) => {
    return function AuthComponent(props){
        const [isAuthenticated, setIsAuthenticated] = useState(false)

        useEffect(() => {
            const token = document.cookie.split('; ').find(row => row.startsWith('token='))
            if(token){
                setIsAuthenticated(true);
            }else{
                setIsAuthenticated(false);
            }
        },[]);

        if(isAuthenticated){
            return <wrappedComponent {...props}/>
        }else{
            return <Navigate to="/Login"/>
        }
    };
};

export default withAuthentication