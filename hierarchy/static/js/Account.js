$(document).ready(function() {
    $('#updateButton').click(function() {
        var formData = $('#updateForm').serialize();

        $.ajax({
            type: 'POST',
            url: account,
            data: formData,
            success: function(response) {
                alert('Password updated successfully!');
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);
            }
        });
    });
});