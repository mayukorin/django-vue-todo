import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store";
import Home from "@/views/Home.vue";
//import LoginPage from "@/views/LoginPage.vue";
import TaskCreatePage from "@/views/TaskCreatePage.vue";
import TaskEditPage from "@/views/TaskEditPage.vue";
import UserCreatePage from "@/views/UserCreatePage.vue";
import UserEditPage from "@/views/UserEditPage.vue";
import PasswordUpdatePage from "@/views/PasswordUpdatePage.vue";
import UsernameUpdatePage from "@/views/UsernameUpdatePage.vue";
import EmailUpdatePage from "@/views/EmailUpdatePage.vue";
import Login from "@/components/templates/LoginView";

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
  },{
    path: "/user-create",
    name: "UserCreate",
    component: UserCreatePage,
  },{
    path: "/user-edit",
    name: "UserEdit",
    component: UserEditPage,
    meta: { requiresAuth: true },
  },{
    path: "/password-update",
    name: "PasswordUpdatePage",
    component: PasswordUpdatePage,
    meta: { requiresAuth: true },
  },{
    path: "/email-update",
    name: "EmailUpdatePage",
    component: EmailUpdatePage,
    meta: { requiresAuth: true },
  },{
    path: "/username-update",
    name: "UsernameUpdatePage",
    component: UsernameUpdatePage,
    meta: { requiresAuth: true },
  },
  {
    path: "/task-create",
    name:  "TaskCreate",
    component: TaskCreatePage,
    meta: { requiresAuth: true }, 
  },
  {
    path: "/task-edit/:task_pk",
    name: 'TaskEdit',
    component: TaskEditPage,
    meta: { requiresAuth: true},
  }
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
  console.log(store.state.message.is_show);

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isLoggedIn) {
      console.log("User is not logged in.");
      if (token != null) {
        console.log("Try to renew user info.");
        store
          .dispatch("auth/renew")
          .then(() => {
            console.log("aaannn");
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
