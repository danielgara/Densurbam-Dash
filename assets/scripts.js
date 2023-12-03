function executeOnDOMLoaded() {
    document.getElementById('ssa').addEventListener('click', function() {
        // Execute the JavaScript code directly
        const body = document.querySelector('body');
        if (body) {
            body.classList.toggle('sidebar-toggled');
        }

        const sidebar = document.querySelector('.sidebar');
        if (sidebar) {
            sidebar.classList.toggle('toggled');
        }

        const mainIcon = document.querySelector('#main-icon');
        if (mainIcon) {
            mainIcon.classList.toggle('display-icon-yes');
        }
    });
}

$(document).ready(function() {
    $("#sidebarToggle").on("click", function() {
        alert("Handler for `click` called.");
    });
});