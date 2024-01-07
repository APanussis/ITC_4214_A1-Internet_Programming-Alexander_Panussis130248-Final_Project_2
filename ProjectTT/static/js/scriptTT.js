$(document).ready(function() {
    // Array to store entries
    var entries = [];

    // Function to add an entry to the table
    function addEntry(name, category) {
        var row = '<tr><td>' + name + '</td><td>' + category + '</td><td><button class="btn btn-danger btn-delete">Delete</button></td></tr>';
        $('#entriesTable tbody').append(row);
    }

    // Function to refresh the table with filtered and sorted entries
    function refreshTable(filterCategory) {
        $('#entriesTable tbody').empty();
        // Sort entries by category
        entries.sort(function(a, b) {
            return a.category.localeCompare(b.category);
        });

        $.each(entries, function(index, entry) {
            if (filterCategory === 'all' || entry.category === filterCategory) {
                addEntry(entry.name, entry.category);
            }
        });

        
    }

    // Add entry when the form is submitted
    $('#addForm').submit(function(event) {
        event.preventDefault();
        var name = $('#entryName').val();
        var category = $('#category').val();
        entries.push({ name: name, category: category });
        addEntry(name, category);
        $('#entryName').val('');
    });





    //Sort currently shown entries in table - BEGIN - Panussis

    //variables (cache elements)
    var $table = $('#entriesTable'); //getting table
    var $tableBody = $table.find('tbody'); //getting the body of table
    var rows, sortedRows; //creating a variables to store data of current rows and new sorted rows

    //sort the table row based on the text of the first div
    function sortEntryNameRows(a, b){

        if ( $(a).find('td:first-Child').text() > $(b).find('td:first-Child').text() ) { //previous row is alphabetically superior to next row
            return 1; 
        }
        if ( $(a).find('td:first-Child').text() < $(b).find('td:first-Child').text() ) { //previous row inferior to the next row
            return -1;
        }
        return 0;
    }

    function sortCategoryRows(a, b){

        if ( $(a).find('td:first-Child + td').text() > $(b).find('td:first-Child + td').text() ) { //previous row is alphabetically superior to next row. Adding a 'td' after 'first-Child' to check for 2nd column of tableEntries.
            return 1; 
        }
        if ( $(a).find('td:first-Child + td').text() < $(b).find('td:first-Child + td').text() ) { //previous row inferior to the next row. Adding a 'td' after 'first-Child' to check for 2nd column of tableEntries.
            return -1;
        }
        return 0;
    }

    $("#btnSortAZEntries").on('click', function(){ // give the 'Sort Entries A-Z' button an event for when its clicked

        //get the rows from the table
        rows = $tableBody.find('tr');

        //sort the rows as "sortRows"
        sortedRows = rows.sort(sortEntryNameRows);

        //replace the old rows with the new rows
        $tableBody.remove('tr');
        $tableBody.append(sortedRows);

    });

    $("#btnSortAZCategories").on('click', function(){ // give the 'Sort Categories A-Z' button an event for when its clicked

        //get the rows from the table
        rows = $tableBody.find('tr');

        //sort the rows as "sortRows"
        sortedRows = rows.sort(sortCategoryRows);

        //replace the old rows with the new rows
        $tableBody.remove('tr');
        $tableBody.append(sortedRows);

    });
    //Sort currently shown entries in table - END - Panussis

    




    // Delete entry when the delete button is clicked
    $('#entriesTable').on('click', '.btn-delete', function() {
        var row = $(this).closest('tr');
        var index = row.index();
        entries.splice(index, 1);
        row.remove();
    });

    // Sort and filter entries when the sort category is changed
    $('#sortCategory').change(function() {
        var filterCategory = $(this).val();
        refreshTable(filterCategory);
    });
    
    // Initialize the table with all entries
    refreshTable('all');

});


 