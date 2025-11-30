
$(document).ready(function(){
  
  if ($('#studentTable').length) {
    $('#studentTable').DataTable({
      "pageLength": 10,
      "lengthChange": false,
      "ordering": true
    });
  }

  $('.deleteForm').on('submit', function(e){
    e.preventDefault();
    const form = this;
    Swal.fire({
      title: 'Delete this student?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.isConfirmed) {
        form.submit();
      }
    });
  });

 
  const handleFlashArray = (arr) => {
    if (!arr || !Array.isArray(arr)) return;
    arr.forEach(item => {
     
      const cat = item[0];
      const msg = item[1];
      if (!msg) return;
      if (cat === 'add') Swal.fire('Success', msg, 'success');
      else if (cat === 'edit') Swal.fire('Updated', msg, 'success');
      else if (cat === 'delete') Swal.fire('Deleted', msg, 'success');
      else if (cat === 'error') Swal.fire('Error', msg, 'error');
      else Swal.fire(msg);
    });
  };

  try { handleFlashArray(flashed); } catch(e) {}
  try { handleFlashArray(flashedLocal); } catch(e) {}
});
