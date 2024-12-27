let lastScroll = 0;
const defaultOffset = 1;
const header = document.querySelector('.header');
const pageKey = 'scrollPosition_' + window.location.pathname;


const scrollPosition = () => window.pageYOffset || document.documentElement.scrollTop;
const containHide = () => header.classList.contains('hide');

window.addEventListener('scroll', () => {
    if(scrollPosition() > lastScroll && !containHide() && scrollPosition() > defaultOffset) {
        header.classList.add('hide');
    }
    else if(scrollPosition() < lastScroll && containHide()){
        header.classList.remove('hide');
    }

    lastScroll = scrollPosition();
})

window.onload = function() {
        if (localStorage.getItem(pageKey)) {
            window.scrollTo(0, localStorage.getItem(pageKey));
        }

        window.addEventListener('beforeunload', function () {
            localStorage.setItem(pageKey, window.scrollY);
        });
};

function openNav() {
    document.getElementById("sideNav").classList.add("active");;
}

function closeNav() {
    document.getElementById("sideNav").classList.remove("active");
}
