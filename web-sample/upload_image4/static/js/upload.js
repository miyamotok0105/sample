
const $form_file_upload = document.getElementById('form-upload');

$form_file_upload.addEventListener('change', (e) => {
    let type = e.target.type;
    console.log('onChange', type);
    
});


// var btnCust = '<button type="button" class="btn btn-secondary" title="Add picture tags" ' + 
//     'onclick="alert(\'Call your custom code here.\')">' +
//     '<i class="glyphicon glyphicon-tag"></i>' +
//     '</button>'; 

// $("#avatar-2").fileinput({
//     overwriteInitial: true,
//     maxFileSize: 1500,
//     showClose: false,
//     showCaption: false,
//     showBrowse: false,
//     browseOnZoneClick: true,
//     removeLabel: '',
//     removeIcon: '<i class="glyphicon glyphicon-remove"></i>',
//     removeTitle: 'Cancel or reset changes',
//     elErrorContainer: '#kv-avatar-errors-2',
//     msgErrorClass: 'alert alert-block alert-danger',
//     defaultPreviewContent: '<img src="/uploads/default_avatar_male.jpg" alt="Your Avatar"><h6 class="text-muted">Click to select</h6>',
//     layoutTemplates: {main2: '{preview} ' +  btnCust + ' {remove} {browse}'},
//     allowedFileExtensions: ["jpg", "png", "gif"]
// });