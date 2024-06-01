$(document).ready(function() {
    const endpoint = 'http://127.0.0.1:8000/analizar';

    $('#analyzeButton').on('click', function() {
        const text = $('#textInput').val();
        if (text.trim() === "") {
            $('#result').html('<p class="text-danger">Please enter some text to analyze.</p>');
            return;
        }

        $.get(endpoint, { texto: text }, function(data) {
            $('#result').html(`
                <p><strong>Label:</strong> ${data.label}</p>
                <p><strong>Score:</strong> ${data.score.toFixed(2)}</p>
            `);
        }).fail(function() {
            $('#result').html('<p class="text-danger">Error analyzing sentiment. Please try again later.</p>');
        });
    });
});
