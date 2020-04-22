
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
                    <div class="card ">
                        <div class="card-header pads-top-left">
                        <h3 class="text-center font-g">RESULTS</h3>


                        </div>
                        <div class="card-body">
                            <div class="row">

                          


                                <div class="col-lg-12 mb-12 pads-4-left-right-2-top-bottom">
                                    <img src="assets/images/lipt-error.png" class="center-img">
                                    <h5 class="text-center font-g">
                                      
                                            Error uploading file.
                                        
                                    </h5>

                                </div>



                            </div>

                            <!--**
                            <div class="card-body">   
                                <div class="col-lg-12 mb-12 ">
                                    <div class="text-center">
                                        <a href="index.php"><button class="btn btn-lipt mb-2 btnp-01">COMPARE OTHER FILES</button></a>
                                    </div>
                                </div>
                            </div>

                            <div class="card-body pads-top-bottom-2">
                            **!-->
                                <div class="row">
                                    <div class="col-lg-6 mb-4 pads-4-left-right-2-top-bottom text-center">
                                        <a href="check.php"><button class="btn btn-lipt mb-2 btnp-01">BACK TO CHECK PPT</button></a>                                        
                                    </div>
                                    <div class="col-lg-6 mb-4 pads-4-left-right-2-top-bottom text-center">
                                        <a href="tool.php"><button class="btn btn-lipt mb-2 btnp-01">BACK TO COMPARE PPTs</button></a>                                       
                                    </div>
                                </div> 
                            </div>


                            <!--
                            <div>
                                <div>
                                    <div class="text-center">
                                        <button type="submit" class="btn btn-primary mb-2 btnp-01">SEE DETAILED RESULTS</button>
                                    </div>
                                </div>
                            </div>

                            <div>
                                <div>
                                    <div class="text-center">
                                        <a href="index.php"><button class="btn btn-primary mb-2 btnp-01">COMPARE OTHER FILES</button></a>
                                    </div>
                                </div>
                            </div>
                            -->


                        </div>
                    </div>
                </div>


            </div>

        </div>

        <!-- Modal -->

        <div class="modal fade" id="summary">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">PPT Design Summary</h5>
                        <button type="button" class="close" data-dismiss="modal"><span>&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-1">  
                                </div> 

                            <div class="col-lg-3 mb-3 pads-4-left-right-2-top-bottom">   
                                <img src="assets/images/lipt-font.png" class="center-img">                                    
                                <h3 class="text-center">3.66%</h3>
                                <h6 class="text-center font-g">FONT <br>IMPROVEMENT</h6>    
                            </div>

                            <div class="col-lg-3 mb-3 pads-4-left-right-2-top-bottom">   
                                <img src="assets/images/lipt-color.png" class="center-img">                                    
                                <h3 class="text-center">0%</h3>
                                <h6 class="text-center font-g">COLOR <br>IMPROVEMENT</h6>    
                            </div>

                            <div class="col-lg-3 mb-3 pads-4-left-right-2-top-bottom">   
                                <img src="assets/images/lipt-image.png" class="center-img">                                    
                                <h3 class="text-center">0%</h3>
                                <h6 class="text-center font-g">IMAGE <br>IMPROVEMENT</h6>    
                            </div>

                        </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
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