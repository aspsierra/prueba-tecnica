import axios from "axios"

export class Auth {
    API_URL = import.meta.env.VITE_API_URL
    CLIENT_ID = import.meta.env.VITE_GITHUB_CLIENT_ID
    GOOGLE_CALLBACK = import.meta.env.VITE_GOOGLE_CALLBACK_URL
    GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID
    
    GITHUB_AUTH_URL = `https://github.com/login/oauth/authorize?client_id=${this.CLIENT_ID}&scope=user`;
    GOOGLE_AUTH_URL= `https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=${this.GOOGLE_CALLBACK}&prompt=consent&response_type=code&client_id=${this.GOOGLE_CLIENT_ID}&scope=openid%20email%20profile&access_type=offline`;
    
    async loginWithGitHub(){

        window.location.href = this.GOOGLE_AUTH_URL
    }
    
    async exchangeCodeForToken(code) {
        
        if (!code) {
            console.error("Código de autorización vacío o nulo.");
            throw new Error("Código de autorización inválido.");
        }
        
        try {
            const csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)?.[1];
            console.log(document.cookie);
            
            axios.defaults.headers.common['X-CSRFToken'] = csrfToken;
            const response = await axios.post(`http://localhost:8000/api/dj-rest-auth/google/`, {
                code: code,
            }, {
                // headers: {
                //     'X-CSRFToken': csrfToken,
                // },
                //  withCredentials: true
            });

            // const response = await axios.get("http://localhost:8000/api/auth/github/callback/");
            console.log(response);
            

            if (response.data && response.data.access) {
                localStorage.setItem("token", response.data.access);
            } else {
                console.error("Respuesta del servidor inválida:", response);
                throw new Error("Respuesta del servidor inválida.");
            }

            return response;
        } catch (error) {
            console.error("Error intercambiando código por token:", error);
            throw error;
        }
    }

    async logout(){
        localStorage.removeItem('token')
    }
}