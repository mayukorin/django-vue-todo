<template>
    <nav>
        <SnackBar />
        <Appbar @handleDrawer="drawerChange" />
        <Drawer :drawer-notification='drawerNotify' @handleDrawer="drawerChange" />
    </nav>
</template>
<script>
import SnackBar from './SnackBar.vue';
import Appbar from './Appbar.vue';
import Drawer from './Drawer.vue';
export default {
    components: { 
        Appbar,
        Drawer,
        SnackBar
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
