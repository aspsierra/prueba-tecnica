import { Auth } from "@/services/auth";

export function handleGithubCallback(to, from, next) {
  const auth = new Auth()
  const queryParams = to.query;
  console.log('Query parameters:', queryParams);

  auth.exchangeCodeForToken(queryParams.code)
  next('/'); 
}
