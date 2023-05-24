// Event handler for discard btn, resets form
$(document).ready(function () {
    $('#discard-btn').click(function () {
        $('#journal-form').trigger('reset');
    });
});

// Past Journals 
$(document).ready(function () {
    function showJournalEntries() {
        let journalEntries = $('.journal-entry');
        let viewMoreBtn = $('.btn-view-more');
        journalEntries.hide();

        // Show the first 5 journals
        journalEntries.slice(0, 5).show();

        // If more than 5 journals, show View More btn
        if (journalEntries.length > 5) {
            journalEntries.slice(0, 5).show();
            viewMoreBtn.show();
        }

        // Shows the next 5 journals. Hides the View More btn
        // if there are no more journals
        viewMoreBtn.on('click', function (e) {
            e.preventDefault();
            let hiddenEntries = journalEntries.filter(':hidden');
            hiddenEntries.slice(0, 5).slideDown();
            if (hiddenEntries.length <= 5) {
                viewMoreBtn.hide();
            }
        });
    }

    showJournalEntries();
});

// Copied from I Think Therefore I Blog walkthrough messages
$(document).ready(function () {
    // Sets a timeout of 2.5 sec on messages
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 2500);
});
