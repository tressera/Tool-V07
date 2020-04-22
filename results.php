
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
                        <h3 class="text-center font-g">RESULTS</h3>
                        <h5 class="text-center font-g"></h5>
                        <!--<p>Please note that the information content of both files must be the same.<br>
                            This tool is only limited to design enhancement in predicting learning improvements.</p>-->
                        </div>
                        
                        <div class="card-body">
                            <div class="row">

                            <?php
                                $overall_scores = file_get_contents("./_evaluator/scores/overall-scores-v3.json");
                                $json_a = json_decode($overall_scores, true);
                            ?>

                                <div class="col-lg-3 mb-3 ">
                                    <img src="assets/images/lipt-font.png" class="center-img">
                                    <h3 class="text-center">
                                        <?php
                                            echo number_format((float)$json_a["font_style_improvement"] * 100, 2, '.', '');
                                        ?>%
                                    </h3>
                                    <h6 class="text-center font-g">FONT (STYLE)<br>IMPROVEMENT</h6>
                                </div>


                                <div class="col-lg-3 mb-3 ">
                                    <img src="assets/images/lipt-color.png" class="center-img">
                                    <h3 class="text-center">
                                        <?php
                                            echo number_format((float)$json_a["font_color_improvement"] * 100, 2, '.', '');
                                        ?>%
                                    </h3>
                                    <h6 class="text-center font-g">(TEXT) COLOR <br>IMPROVEMENT</h6>
                                </div>


                                <div class="col-lg-3 mb-3 ">
                                    <img src="assets/images/lipt-image.png" class="center-img">
                                    <h3 class="text-center">
                                        <?php
                                            echo number_format((float)$json_a["font_image_improvement"] * 100, 2, '.', '');
                                        ?>%
                                    </h3>
                                    <h6 class="text-center font-g">IMAGE <br>IMPROVEMENT</h6>
                                </div>

                                <div class="col-lg-3 mb-3 ">
                                    <img src="assets/images/lipt-icons-01.png" class="center-img">
                                    <h3 class="text-center">
                                        <?php
                                            echo number_format((float)$json_a["expected_learning_improvement"] * 100, 2, '.', '');
                                        ?>%
                                    </h1>
                                    <h6 class="text-center font-g">EXPECTED LEARNING IMPROVEMENT</h6>
                                </div>


                            </div>
                           
                            <!--*******************
                            <div class="text-center pads-top-bottom-3">
                                <button type="button" class="btn btn-lipt mb-2 btnp-01" data-toggle="modal" data-target="#summary">SEE OTHER CHANGES</button>
                            </div>
                            ********************-->
                               
                           
                        </div>
                    </div>
                </div>

                <div class="card-body">
                    <div class="row">

                        <div class="col-3">
                        </div>

                        <div class="col-lg-3 mb-4 ">
                            <div class="text-center">
                                <a href="index.php"><button class="btn btn-lipt mb-2 btnp-01">HOME</button></a>
                            </div>
                        </div>
                        <div class="col-lg-3 mb-4 ">
                            <div class="text-center">
                                <a href="tool.php"><button class="btn btn-lipt mb-2 btnp-01">COMPARE OTHER FILES</button></a>
                            </div>
                        </div>

                        <div class="col-3">
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