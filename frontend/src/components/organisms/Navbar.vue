<template>
    <nav>
        <Appbar @handleDrawer="drawerChange" />
        <Drawer :drawer-notification='drawerNotify' @handleDrawer="drawerChange" />
    </nav>
</template>
<script>
import Appbar from './Appbar.vue';
import Drawer from './Drawer.vue';
export default {
    components: { 
        Appbar,
        Drawer 
    },
    data() {
        return {
            drawerNotify: false,
        }
    },
    methods: {
        drawerChange() {
            this.drawerNotify = !this.drawerNotify;
        }
    },
};
</script>
