
<!DOCTYPE html>
<html lang="en">

<head>

<?php include('imports/head.php') ?>

</head>

<body>

    <!--*******************
        Preloader start
    ********************-->

    <!--
    <div id="preloader">
        <div class="loader"></div>
    </div>
    -->

    <!--*******************
        Preloader end
    ********************-->


    <!--**********************************
        Main wrapper start
    ***********************************-->
    <div id="main-wrapper">

        <!--**********************************
            Nav header start
        ***********************************-->



        <!--**********************************
            Nav header end
        ***********************************-->

        <!--**********************************
            Header start
        ***********************************-->

        <!--**********************************
            Header end ti-comment-alt
        ***********************************-->

        <!--**********************************
            Sidebar start
        ***********************************-->



        <!--**********************************
            Sidebar end
        ***********************************-->

        <!--**********************************
            Content body start
        ***********************************-->
        <div class="content-body c-body-1">


            <div class="container-fluid">

                <div class="row">

                    <div class="col-12">
                    <!--<span class="brand-title"><b><img src="../assets/images/Logo.png" width="375px;" height="175px;"></b></span>-->
                    </div>

                </div>

                <div class="row justify-content-between mb-3 header-01">
					<div class="card-body col-12 text-center">
						<h2 class="page-heading-01">Learning Improvement Prediction Tool</h2>
						<h5 class="p-header">A tool that will predict learning improvement based on the Powerpoint Presesentation design enhancements.
                        </h5>
					</div>
                </div>

                <div class="col-xl-6 col-xxl-12 pads-4-left-right-2-top-bottom">
                    <div class="card">
                        <div class="card-header pads-top-left">
                        <h3 class="text-center font-g">INSTRUCTION</h3>
                        <h5 class="text-center font-g">Upload your PPT below.</h5>
                        <!--<p>Please note that the information content of both files must be the same.<br>
                            This tool is only limited to design enhancement in predicting learning improvements.</p>-->
                        </div>
                        <div class="card-body pads-top-bottom-5">
                            <form action="upload-checker.php" method="post" enctype="multipart/form-data" muliple>
                                <div class="row">
                                    <div class="col-lg-3 mb-4 pads-4-left-right-2-top-bottom">
                                    </div>
                                    <div class="col-lg-6 mb-4 pads-4-left-right-2-top-bottom">
                                        
                                        <input type="file" class="dropify" name="targetFile[]" required="" />
                                    </div>
                                    <div class="col-lg-3 mb-4 pads-4-left-right-2-top-bottom">
                                    </div>
                                </div>
                                <div class="col-auto text-center">
                                <button class="btn btn-lipt mb-2 btnp-01" type="submit">SUBMIT</button>
                               </div>
                               
                           </form>
                        </div>
                    </div>
                </div>

                <div class="text-center pads-top-bottom-5">
                    <a href="index.php"><button class="btn btn-lipt mb-2 btnp-01">HOME</button></a>
                </div>


            </div>

        </div>
        <!--**********************************
            Content body end
        ***********************************-->


        <!--**********************************
            Footer start
        ***********************************-->

        <?php include('imports/footer.php') ?>

        <!--**********************************
            Footer end
        ***********************************-->


        <!--**********************************
            Right sidebar start
        ***********************************-->

        <!--**********************************

        ***********************************-->

        <!--**********************************
            Right sidebar end
        ***********************************-->
    </div>
    <!--**********************************
        Main wrapper end
    ***********************************-->

    <!--**********************************
        Scripts
    ***********************************-->

    <?php include('imports/scripts.php') ?>

</body>

</html>