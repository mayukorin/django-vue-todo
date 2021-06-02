import Vue from "vue";
import Vuex from "vuex";
import api from "@/services/api";

Vue.use(Vuex);

const authModule = {
  namespaced: true,
  state: {
    email: "",
    username: "",
    isLoggedIn: false,
  },
  mutations: {
    set(state, payload) {
      state.email = payload.user.email;
      state.username = payload.user.username;
      state.isLoggedIn = true;
    },
    clear(state) {
      state.email = "";
      state.username = "";
      state.isLoggedIn = false;
    },
  },
  actions: {
    login(context, payload) {
      console.log("aaaa");
      console.log(payload.email);
      console.log(payload.password);
      console.log("ここから行かない?");
      return api
        .post("/auth/jwt/create/", {
          email: payload.email,
          password: payload.password,
        })
        .then((response) => {
          console.log(response.data.access);
          localStorage.setItem("access", response.data.access);
          return context.dispatch("renew");
        });
    },
    logout(context) {
      localStorage.removeItem("access");
      context.commit("clear");
    },
    renew(context) {
      return api.get("/auth/users/me/").then((response) => {
        const user = response.data;
        console.log("data");
        console.log(user);
        context.commit("set", { user: user });
      });
    },
    signup(context, payload) {
      return api({
        method: "post",
        url: "/user/create/",
        data: {
          email: payload.email,
          username: payload.username,
          password: payload.password
        }
      }).then((response) => {
        console.log(response.data);
        return context.dispatch("login", {email: response.data.email, password: payload.password})
      })
    },
    userNameUpdate(context, payload) {
      console.log("What...")
      console.log(payload);
      return api({
          method: "patch",
          url: "user/profile/update/",
          data: {
              username: payload.username,
              confirm_password: payload.confirm_password
          }
        }).then(response => {
          const password = payload.confirm_password;
          context.dispatch("logout");
          return context.dispatch("login", {email: response.data.email, password: password});
          /*
          //ログイン
          return api
          .post("/auth/jwt/create/", {
            email: response.data.email,
            password: password,
          })
          .then((response) => {
            localStorage.setItem("access", response.data.access);
            return context.dispatch("renew");
          });
          */
        })
    },
    emailUpdate(context, payload) {
      return api({
        method: "patch",
        url: "user/profile/update/",
        data: {
          email: payload.email,
          confirm_password: payload.confirm_password
        }
      }).then(response => {
        const password = payload.confirm_password;
        context.dispatch("logout");
        return context.dispatch("login", {email: response.data.email, password: password});
      })
    },
    passwordUpdate(context, payload) {
      return api({
        method: "patch",
        url: "/password/update/",
        data: {
            confirm_password: payload.confirm_password,
            password: payload.new_password
        }
      }).then(response => {
        const password = payload.new_password;
        const email = response.data.email;
        context.dispatch("logout");
        return context.dispatch("login", {email: email, password: password});
      })
    }
  },
};

const messageModule = {
  namespaced: true,
  state: {
    error: "",
    warnings: [],
    info: "",
    keep_info: "",
    is_show: false,
    show_flag: false,
    color:"",
  },
  mutations: {
    set(state, payload) {
      if (payload.error) {
        state.error = payload.error;
        state.color = "error";
      }
      if (payload.warnings) {
        state.warnings = payload.warnings;
        state.color = "warning";
      }
      if (payload.info) {
        state.info = payload.info;
        state.color = "success";
      }
      if (payload.keep_info) {
        state.keep_info = payload.keep_info;
      }
    },
    clear(state) {
      state.error = "";
      state.warnings = [];
      state.info = "";
      state.color = "";
    },
    clear_keep_info_message(state) {
      state.keep_info = "";
    },
    set_is_show_true(state) {
      state.is_show = true;
    },
    set_is_show_false(state) {
      state.is_show = false;
    },
    set_show_flag_true(state) {
      console.log("why");
      state.show_flag = true;
    },
    set_show_flag_false(state) {
      console.log("zero");
      state.show_flag = false;
    },
  },
  actions: {
    setErrorMessage(context, payload) {
      context.commit("clear");
      console.log("56");
      context.commit("set", { error: payload.message });
    },
    setWarningMessages(context, payload) {
      context.commit("clear");
      context.commit("set", { warnings: payload.messages });
    },
    setInfoMessage(context, payload) {
      context.commit("clear");
      context.commit("set", { info: payload.message });
    },
    setKeepInfoMessage(context, payload) {
      console.log("wowo");
      console.log(payload.message);
      context.commit("set", { keep_info: payload.message });
    },
    clearKeepInfoMessage(context) {
      context.commit("clear_keep_info_message");
    },
    clearMessages(context) {
      context.commit("clear");
    },
    setIsShowTrue(context) {
      context.commit("set_is_show_true");
    },
    setIsShowFalse(context) {
      context.commit("set_is_show_false");
    },
    setShowFlagTrue(context) {
      context.commit("set_show_flag_true");
    },
    setShowFlagFalse(context) {
      context.commit("set_show_flag_false");
    }
  },
};

const taskModule = {
  namespaced: true,
  state: {
    tasks: [],
    update_flag: false,
  },
  getters: {
    update_flag(state) {
      return state.update_flag;
    }
  },
  mutations: {
    set(state, payload) {
      state.tasks = payload;
    },
    addTask(state, payload) {
      state.tasks.push(payload);
    },
    set_update_true(state) {
      state.update_flag = true;
    },
    set_update_false(state) {
      state.update_flag = false;
    },
    fetchTaskList(state, payload) {
      state.tasks = payload.taskList;
    },
    AddTask(state, payload) {
      state.tasks.push(payload);
    },
    UpdateTask(state, payload) {
      const task = state.tasks.find(task => task.pk === payload.pk);
      task.title = payload.title;
      task.content = payload.content;
      task.deadline = payload.deadline;
    },
    DeleteTask(state, payload) {
      const task = state.tasks.find(task => task.pk === payload.pk);
      state.tasks.splice(state.tasks.indexOf(task), 1)
    }
  },
  actions: {
    setTasks(context, payload) {
      context.commit("set", payload);
    },
    /*
    addTask(context, payload) {
      context.commit("addTask", payload);
    },
    */
    setUpdateFlagTrue(context) {
      context.commit("set_update_true");
    },
    setUpdateFlagFalse(context) {
      context.commit("set_update_false");
    },
    fetchList(context) {
      return api.get("/task/list/").then((response) => {
        console.log(response.data);
        context.commit("fetchTaskList", { taskList: response.data });
      });
    },
    addTask(context, payload) {
      return api({
        method: "post",
        url: "/task/create/",
        data: {
            title: payload.title,
            content: payload.content,
            deadline: payload.deadline,
        }
      }).then((response) => {
        console.log(response.data);
        context.commit("AddTask", response.data);
      })
    },
    updateTask(context, payload) {
      return api({
        method: "patch",
        url: `/task/update/${payload.pk}/`,
        data: {
          title: payload.title,
          content: payload.content,
          deadlie: payload.deadline
        }
      }).then((response) => {
        console.log(response.data);
        context.commit("UpdateTask", response.data);
      })
    },
    deleteTask(context, payload) {
      return api({
        method: "delete",
        url: `task/delete/${payload.pk}/`,
      }).then((response) => {
        console.log(response);
        context.commit("DeleteTask", payload);
      })
    }
  }
}

const store = new Vuex.Store({
  modules: {
    auth: authModule,
    message: messageModule,
    task: taskModule,
  },
});

export default store;
