pipeline {

    agent { label 'jenkins-worker' }

    options {
        timestamps()
        timeout(75)
    }

    stages {
        stage('Run Tests') {
            parallel {
                stage('lms_unit_1') {
                    agent { label "jenkins-worker" }
                    environment {
                        SHARD = 1
                        TEST_SUITE = 'lms-unit'
                    }
                    steps {
                        sshagent(credentials: ['jenkins-worker'], ignoreMissing: true) {
                            checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']],
                                doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [],
                                userRemoteConfigs: [[credentialsId: 'jenkins-worker', refspec: '+refs/heads/master:refs/remotes/origin/master',
                                url: 'git@github.com:edx/edx-platform.git']]]
                            sh "bash scripts/all-tests.sh"
                        }
                    }
                    post {
                        always {
                            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**/*,test_root/log/**/*.log,**/nosetests.xml,*.log'
                            junit '**/nosetests.xml'
                        }
                    }
                }
                stage('lms_unit_2') {
                    agent { label "jenkins-worker" }
                    environment {
                        SHARD = 2
                        TEST_SUITE = 'lms-unit'
                    }
                    steps{
                        sshagent(credentials: ['jenkins-worker'], ignoreMissing: true) {
                            checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']],
                                doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [],
                                userRemoteConfigs: [[credentialsId: 'jenkins-worker', refspec: '+refs/heads/master:refs/remotes/origin/master',
                                url: 'git@github.com:edx/edx-platform.git']]]
                            sh "bash scripts/all-tests.sh"
                        }
                    }
                    post {
                        always {
                            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**/*,test_root/log/**/*.log,**/nosetests.xml,*.log'
                            junit '**/nosetests.xml'
                        }
                    }
                }
                stage('lms_unit_3') {
                    agent { label "jenkins-worker" }
                    environment {
                        SHARD = 3
                        TEST_SUITE = 'lms-unit'
                    }
                    steps {
                        sshagent(credentials: ['jenkins-worker'], ignoreMissing: true) {
                            checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']],
                                doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [],
                                userRemoteConfigs: [[credentialsId: 'jenkins-worker', refspec: '+refs/heads/master:refs/remotes/origin/master',
                                url: 'git@github.com:edx/edx-platform.git']]]
                            sh "bash scripts/all-tests.sh"
                        }
                    }
                    post {
                        always {
                            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**/*,test_root/log/**/*.log,**/nosetests.xml,*.log'
                            junit '**/nosetests.xml'
                        }
                    }
                }
                stage('lms_unit_4') {
                    agent { label "jenkins-worker" }
                    environment {
                        SHARD = 4
                        TEST_SUITE = 'lms-unit'
                    }
                    steps {
                        sshagent(credentials: ['jenkins-worker'], ignoreMissing: true) {
                            checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']],
                                doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [],
                                userRemoteConfigs: [[credentialsId: 'jenkins-worker', refspec: '+refs/heads/master:refs/remotes/origin/master',
                                url: 'git@github.com:edx/edx-platform.git']]]
                            sh "bash scripts/all-tests.sh"
                        }
                    }
                    post {
                        always {
                            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**/*,test_root/log/**/*.log,**/nosetests.xml,*.log'
                            junit '**/nosetests.xml'
                        }
                    }
                }
                stage('cms_unit') {
                    agent { label "jenkins-worker" }
                    environment {
                        SHARD = 1
                        TEST_SUITE = 'cms-unit'
                    }
                    steps {
                        sshagent(credentials: ['jenkins-worker'], ignoreMissing: true) {
                            checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']],
                                doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [],
                                userRemoteConfigs: [[credentialsId: 'jenkins-worker', refspec: '+refs/heads/master:refs/remotes/origin/master',
                                url: 'git@github.com:edx/edx-platform.git']]]
                            sh "bash scripts/all-tests.sh"
                        }
                    }
                    post {
                        always {
                            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**/*,test_root/log/**/*.log,**/nosetests.xml,*.log'
                            junit '**/nosetests.xml'
                        }
                    }
                }
                stage('commonlib_unit') {
                    agent { label "jenkins-worker" }
                    environment {
                        SHARD = 1
                        TEST_SUITE = 'commonlib-unit'
                    }
                    steps {
                        sshagent(credentials: ['jenkins-worker'], ignoreMissing: true) {
                            checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']],
                                doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [],
                                userRemoteConfigs: [[credentialsId: 'jenkins-worker', refspec: '+refs/heads/master:refs/remotes/origin/master',
                                url: 'git@github.com:edx/edx-platform.git']]]
                            sh "bash scripts/all-tests.sh"
                        }
                    }
                    post {
                        always {
                            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**/*,test_root/log/**/*.log,**/nosetests.xml,*.log'
                            junit '**/nosetests.xml'
                        }
                    }
                }
            }
        }
    }
}
