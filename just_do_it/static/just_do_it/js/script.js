function submitCreateForm() {
    const form_create = document.forms['id_form_create'];
    if (form_create.reportValidity()) {
        if (confirm("Create this task?") === true) {
            form_create.submit();
        } else {
            return false;
        }
    }
}

function submitDeleteForm() {
    const form_delete = document.forms['id_form_delete'];
    if (form_delete.reportValidity()) {
        if (confirm("Delete this task?") === true) {
            form_delete.submit();
        } else {
            return false;
        }
    }
}

function submitUpdateForm() {
    const form_update = document.forms['id_form_update'];
    if (form_update.reportValidity()) {
        if (confirm("Update this task?") === true) {
            form_update.submit();
        } else {
            return false;
        }
    }
}

function markComplete() {
    const form_update = document.forms['id_form_update'];
    const checkbox = document.getElementById('id_completed');
    if (form_update.reportValidity()) {
        if (confirm("Mark task as completed?") === true) {
            checkbox.click();
            form_update.submit();
        } else {
            return false;
        }
    }
}

function markIncomplete() {
    const form_update = document.forms['id_form_update'];
    const checkbox = document.getElementById('id_completed');
    if (form_update.reportValidity()) {
        if (confirm("Mark task as incomplete?") === true) {
            checkbox.click();
            form_update.submit();
        } else {
            return false;
        }
    }
}
