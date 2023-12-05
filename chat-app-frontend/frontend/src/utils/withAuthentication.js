import React, { useEffect } from "react";
import { useState } from "react"
import Navigate from "../Components/Navigate";


const withAuthentication = (WrappedComponent) => {
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
            return <WrappedComponent {...props}/>
        }else{
            return <Navigate to="/Login"/>
        }
    };
};

export default withAuthentication