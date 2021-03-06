import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store";
//import TaskCreatePage from "@/views/TaskCreatePage";
//import TaskEditPage from "@/views/TaskEditPage";
import UserProfile from "@/components/templates/UserProfileView";
import PasswordUpdate from "@/components/templates/PasswordUpdateView";
import UserNameUpdate from "@/components/templates/UserNameUpdateView";
import EmailUpdate from "@/components/templates/EmailUpdateView";
import Login from "@/components/templates/LoginView";
import Home from "@/components/templates/HomeView";
import UserCreate from "@/components/templates/UserCreateView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/user-create",
    name: "UserCreate",
    component: UserCreate,
  },
  {
    path: "/user-profile",
    name: "UserProfile",
    component: UserProfile,
    meta: { requiresAuth: true },
  },
  {
    path: "/password-update",
    name: "PasswordUpdate",
    component: PasswordUpdate,
    meta: { requiresAuth: true },
  },
  {
    path: "/email-update",
    name: "EmailUpdate",
    component: EmailUpdate,
    meta: { requiresAuth: true },
  },
  {
    path: "/username-update",
    name: "UsernameUpdate",
    component: UserNameUpdate,
    meta: { requiresAuth: true },
  },
  {
    path: "*",
    component: Login,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.state.auth.isLoggedIn;
  const token = localStorage.getItem("access");
  console.log("to.path=", to.path);
  console.log("isLoggedIn=", isLoggedIn);

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isLoggedIn) {
      console.log("User is not logged in.");
      if (token != null) {
        console.log("Try to renew user info.");
        store
          .dispatch("auth/renew")
          .then(() => {
            console.log("Succeeded to renew. So, free to next.");
            next();
          })
          .catch(() => {
            forceToLoginPage(to);
          });
      } else {
        forceToLoginPage(to);
      }
    } else {
      console.log("User is already logged in. So, free to next.");
      next();
    }
  } else {
    console.log("Go to public page.");
    next();
  }
});

function forceToLoginPage(to) {
  console.log("Force to login page.");
  router.replace({
    path: "/login",
    query: { next: to.fullPath },
  });
}

export default router;
