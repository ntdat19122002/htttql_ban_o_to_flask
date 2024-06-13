import Admin from '../views/Admin/Admin.vue'
import AdminLivetime from '../views/Admin/AdminLivetime.vue'
import AdminOto from '../views/Admin/AdminOto.vue'
import AdminHoadon from '../views/Admin/AdminHoadon.vue'
import AdminHoadontemp from '../views/Admin/AdminHoadontemp.vue'
import AdminLoaixe from '../views/Admin/AdminLoaixe.vue'
import AdminNguoidung from '../views/Admin/AdminNguoidung.vue'
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
    },
    {
        path: '/admin/hoadon',
        name: 'admin_hoadon',
        component: AdminHoadon
    },
    {
        path: '/admin/hoadontemp',
        name: 'admin_hoadontemp',
        component: AdminHoadontemp
    },
    {
        path: '/admin/loaixe',
        name: 'admin_loaixe',
        component: AdminLoaixe
    },
    {
        path: '/admin/nguoidung',
        name: 'admin_nguoidung',
        component: AdminNguoidung
    }
]

export default admin_route