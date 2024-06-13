import Admin from '../views/Admin/Admin.vue'
import AdminLivetime from '../views/Admin/AdminLivetime.vue'
import AdminOto from '../views/Admin/AdminOto.vue'
const admin_route = [
    {
        path: '/admin',
        name: 'admin',
        component: Admin
    },
    {
        path: '/admin/livetime',
        name: 'admin_livetime',
        component: AdminLivetime
    },
    {
        path: '/admin/oto',
        name: 'admin_oto',
        component: AdminOto
    }
]

export default admin_route