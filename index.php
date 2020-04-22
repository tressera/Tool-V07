
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

                <div class="col-xl-6 col-xxl-12 pads-4-left-right-2-top-bottom pads-bottom-5">
                    <div class="card">
                        <div class="card-header pads-top-left">
                        <h3 class="text-center font-g">INSTRUCTIONS</h3>
                        <h5 class="text-center font-g">Check your PPT below and check if it follows the guidelines 
                            <br>or compare your original and modified PPT and predict learning improvement.</h5>
                        <!--<p>Please note that the information content of both files must be the same.<br>
                            This tool is only limited to design enhancement in predicting learning improvements.</p>-->
                        </div>
                        <div class="card-body pads-top-bottom-2">
                            
                                <div class="row">
                                    <div class="col-lg-6 mb-4 pads-4-left-right-2-top-bottom text-center">
                                        <img src="assets/images/lipt-check.png" class="center-img-comp">                                       
                                        <a href="check.php"><button class="btn btn-lipt-02 mb-2 btnp-02">CHECK PPT</button></a>                                        
                                    </div>
                                    <div class="col-lg-6 mb-4 pads-4-left-right-2-top-bottom text-center">
                                        <img src="assets/images/lipt-compare.png" class="center-img-comp">
                                        <a href="tool.php"><button class="btn btn-lipt-02 mb-2 btnp-02">COMPARE PPTs</button></a>                                       
                                    </div>
                                </div>
                               
                           
                        </div>
                    </div>
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