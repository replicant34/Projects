     var sideBarisOpen = true;

    toggleBtn.addEventListener( 'click', (event) => {
        event.preventDefault();

            if(sideBarisOpen){
                dashboard_sidebar.style.width = '10%';
                dashboard_sidebar.style.transition = '0.5s all';
                dashboard_content_container.style.width = '90%';
                dashboard_logo.style.fontSize = '15px';
                userImage.style.width = '60px';

                menuIcons = document.getElementsByClassName('menuText');
                for(var i=0; i < menuIcons.length;i++){
                    menuIcons[i].style.display = 'none';
                }

                document.getElementsByClassName('dashboard_menu_lists')[0].style.textAlign = 'center';
                sideBarisOpen = false;
             } else {
                dashboard_sidebar.style.width = '20%';
                dashboard_content_container.style.width = '80%';
                dashboard_logo.style.fontSize = '25px';
                userImage.style.width = '80px';

                menuIcons = document.getElementsByClassName('menuText');
                for(var i=0; i < menuIcons.length;i++){
                    menuIcons[i].style.display = 'inline-block';
                }

                document.getElementsByClassName('dashboard_menu_lists')[0].style.textAlign = 'left';
                 sideBarisOpen = true;
             }
             
    });


// Submenu function show hide

document.addEventListener('click', function(e) {
    let clickedEl = e.target;

    if (clickedEl.classList.contains('showHideSubmenu')) {
        let subMenu = clickedEl.closest('li').querySelector('.subMenus');
        let mainMenuIcon = clickedEl.closest('li').querySelector('.mainMenuIconAngle');

        if (subMenu != null) {
            if (subMenu.style.display === 'block') {
                subMenu.style.display = 'none';
                mainMenuIcon.classList.remove('fa-angle-down');
                mainMenuIcon.classList.add('fa-angle-up');
            } else {
                subMenu.style.display = 'block';
                mainMenuIcon.classList.remove('fa-angle-up');
                mainMenuIcon.classList.add('fa-angle-down');
            }
        }
    }
});



