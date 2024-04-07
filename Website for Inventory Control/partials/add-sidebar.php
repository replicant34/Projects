<div class="dashboard-sidebar" id="dashboard_sidebar">
            <h3 class="dashboard_logo" id="dashboard_logo">Stock Control</h3>
            <div class="dashboard-sidebar_user">
                <img src="Imeges/IMG_6234.jpeg" alt="User image" id="userImage"/>
                <span><?= $user['first_name'] . ' '. $user['last_name'] ?></span>
            </div>
            <div class="dashboard-sidebar_menus">
                <ul class="dashboard_menu_lists">
                    <!-- class="menuActive" -->
                    <li class="liMainMenu">
                        <a href="./dusboard.php"><i class="fa fa-dashboard"></i><span class="menuText">Dashboard</span></a>
                    </li>
                    <li class="liMainMenu">
                        <a href="javascript:void(0);" class="showHideSubmenu">
                            <i class="fa fa-box showHideSubmenu"></i> 
                            <span class="menuText showHideSubmenu">Products</span>
                            <i class="fa fa-angle-down mainMenuIconAngle showHideSubmenu"></i>
                        </a>
                        <ul class="subMenus">
                            <li><a class="subMenuLink" href="./products-view.php"><i class="fa fa-user-point"></i><span class="menuText">View products</span></a></li>
                            <li><a class="subMenuLink" href="./product-add.php"><i class="fa fa-user-point"></i><span class="menuText">Add product</span></a></li>
                        </ul>
                    </li>
                    <li class="liMainMenu">
                        <a href="javascript:void(0);" class="showHideSubmenu">
                            <i class="fa fa-truck showHideSubmenu"></i> 
                            <span class="menuText showHideSubmenu">Suppliers</span>
                            <i class="fa fa-angle-down mainMenuIconAngle showHideSubmenu"></i>
                        </a>
                        <ul class="subMenus">
                            <li><a class="subMenuLink" href="#"><i class="fa fa-user-point-o"></i><span class="menuText">View suppliers</span></a></li>
                            <li><a class="subMenuLink" href="#"><i class="fa fa-user-point-o"></i><span class="menuText">Add supplier</span></a></li>
                        </ul>
                    </li>
                    <li class="liMainMenu showHideSubmenu">
                        <a href="javascript:void(0);" class="showHideSubmenu">
                            <i class="fa fa-user-plus showHideSubmenu"></i> 
                            <span class="menuText showHideSubmenu">Add User</span>
                            <i class="fa fa-angle-down mainMenuIconAngle showHideSubmenu"></i>
                        </a>
                        <ul class="subMenus">
                            <li><a class="subMenuLink" href="./users-view.php"><i class="fa fa-user-circle-o"></i><span class="menuText">View Users</span></a></li>
                            <li><a class="subMenuLink" href="./users-add.php"><i class="fa fa-user-circle-o"></i><span class="menuText">Add Users</span></a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>